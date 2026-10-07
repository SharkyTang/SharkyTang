#!/usr/bin/env python3
"""Render real GitHub contribution counts without third-party dependencies."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import tempfile
import urllib.error
import urllib.request

QUERY = '''query($login: String!) {
  user(login: $login) { contributionsCollection { contributionCalendar {
    weeks { contributionDays { date contributionCount } }
  } } }
}'''
COLORS = ['#101F30', '#163F69', '#2266A1', '#3994D7', '#78C9FF']


def calendar(response):
    if response.get('errors'):
        raise ValueError('GitHub returned GraphQL errors; keeping existing assets.')
    weeks = response['data']['user']['contributionsCollection']['contributionCalendar']['weeks'][-26:]
    if len(weeks) != 26:
        raise ValueError('Expected 26 weeks of contribution data.')
    previous = None
    for index, week in enumerate(weeks):
        days = week['contributionDays']
        if not 1 <= len(days) <= 7 or (index < 25 and len(days) != 7):
            raise ValueError('Invalid contribution week.')
        if dt.date.fromisoformat(days[0]['date']).weekday() != 6:
            raise ValueError('Contribution weeks must start on Sunday.')
        for day in days:
            date = dt.date.fromisoformat(day['date'])
            count = day['contributionCount']
            if type(count) is not int or count < 0:
                raise ValueError('Invalid contribution count.')
            if previous and date != previous + dt.timedelta(days=1):
                raise ValueError('Contribution dates must be consecutive.')
            if date > dt.datetime.now(dt.timezone.utc).date():
                raise ValueError('Unexpected future contribution date.')
            previous = date
    return weeks


def text(x, y, value, size=24, color='#D6E7FF'):
    # Only fixed strings, dates and numbers are rendered; API free text is excluded.
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}">{value}</text>'


def render(weeks, mobile=False):
    width, height = (600, 630) if mobile else (1200, 400)
    days = [d for w in weeks for d in w['contributionDays']]
    total = sum(d['contributionCount'] for d in days)
    start, end = days[0]['date'], days[-1]['date']
    updated = dt.datetime.now(dt.timezone.utc).date().isoformat()
    peak = max(d['contributionCount'] for d in days)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
           '<title id="title">SharkyTang — GitHub activity</title>',
           f'<desc id="desc">{total} GitHub contributions from {start} to {end}. Updated {updated}. Counts come from GitHub GraphQL.</desc>',
           f'<rect x="1" y="1" width="{width-2}" height="{height-2}" rx="16" fill="#050B12" stroke="#183A5A" stroke-width="2"/>',
           '<g font-family="Menlo,Consolas,monospace">',
           text(32, 48, '&gt; contribution_history', 26, '#58A6FF'),
           text(32, 89, f'{total} contributions · last 26 weeks', 25),
           text(32, 126 if mobile else 122, f'{start} — {end}', 24, '#8FA8C5')]
    groups = [weeks[:13], weeks[13:]] if mobile else [weeks]
    for group_index, group in enumerate(groups):
        base_y = 183 + group_index * 191 if mobile else 157
        gap, row_gap = (34, 21) if mobile else (39, 21)
        if mobile:
            out.append(text(32, base_y - 17, group[0]['contributionDays'][0]['date'][:7], 23, '#8FA8C5'))
        for col, week in enumerate(group):
            for day in week['contributionDays']:
                date = dt.date.fromisoformat(day['date'])
                row = (date.weekday() + 1) % 7
                count = day['contributionCount']
                level = 0 if count == 0 else min(4, max(1, (count * 4 + peak - 1) // max(1, peak)))
                out.append(f'<rect x="{90+col*gap}" y="{base_y+row*row_gap}" width="18" height="18" rx="3" fill="{COLORS[level]}"><title>{day["date"]}: {count} contributions</title></rect>')
        for row, label in [(1, 'Mon'), (3, 'Wed'), (5, 'Fri')]:
            out.append(text(32, base_y+row*row_gap+14, label, 17, '#8FA8C5'))
    footer_y = height - 57
    out.append(text(32, footer_y, f'Updated {updated} · GitHub API', 22, '#8FA8C5'))
    legend_x, legend_y = (320, height-28) if mobile else (876, footer_y)
    out.append(text(legend_x-65, legend_y, 'Less', 18, '#8FA8C5'))
    for index, color in enumerate(COLORS):
        out.append(f'<rect x="{legend_x+index*23}" y="{legend_y-14}" width="16" height="16" rx="3" fill="{color}"/>')
    out.append(text(legend_x+124, legend_y, 'More', 18, '#8FA8C5'))
    out.append('</g></svg>\n')
    return '\n'.join(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, help='Existing GitHub GraphQL response')
    parser.add_argument('--output-dir', type=Path, default=Path(__file__).resolve().parents[1] / 'assets')
    args = parser.parse_args()
    if args.input:
        response = json.loads(args.input.read_text())
    else:
        token = os.environ.get('GH_TOKEN')
        if not token:
            raise ValueError('Set GH_TOKEN to read GitHub GraphQL; keeping existing assets.')
        request = urllib.request.Request('https://api.github.com/graphql',
            data=json.dumps({'query': QUERY, 'variables': {'login': 'SharkyTang'}}).encode(),
            headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json', 'User-Agent': 'SHARKY.OS-profile'})
        try:
            with urllib.request.urlopen(request, timeout=30) as result:
                response = json.load(result)
        except urllib.error.HTTPError as error:
            raise ValueError(f'GitHub HTTP {error.code}; keeping existing assets.') from None
    weeks = calendar(response)
    # Validate and render both outputs before replacing either existing asset.
    outputs = {'activity.svg': render(weeks), 'activity-mobile.svg': render(weeks, True)}
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, content in outputs.items():
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=args.output_dir, delete=False) as output:
            output.write(content)
            temporary = Path(output.name)
        temporary.chmod(0o644)
        temporary.replace(args.output_dir / name)
    print('Updated two contribution assets from verified GitHub data.')


if __name__ == '__main__':
    try:
        main()
    except (ValueError, KeyError, TypeError, OSError) as error:
        raise SystemExit(f'Activity update failed: {error}') from None
