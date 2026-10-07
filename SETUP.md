# SHARKY.OS Profile

This profile uses GitHub-supported Markdown, HTML, `<picture>` and self-contained SVGs. There is no website build or browser JavaScript to deploy.

## Preview and publish

1. Open `README.md` in a Markdown preview, or preview the changed file on GitHub.
2. Check wide and narrow layouts. Below a 700 px viewport, `<picture>` selects mobile artwork; images use `width="100%"`.
3. Commit reviewed changes and push to this repository's default branch to update [the profile](https://github.com/SharkyTang).

## Activity refresh

`.github/workflows/profile-activity.yml` refreshes 26 weeks of contribution data daily and supports manual runs. It uses the built-in `GITHUB_TOKEN`, GitHub GraphQL, Python's standard library and a pinned official checkout Action. No personal token or package installation is needed.

Permissions default to read-only; only the update job can write repository contents. Only the two activity SVGs are committed. API errors leave the last chart in place, with its update date and link to live GitHub history.

For a local refresh, set `GH_TOKEN` through your existing secure credential mechanism, then run `python3 scripts/update_activity.py`. For offline rendering:

```sh
python3 scripts/update_activity.py --input /path/to/response.json --output-dir /tmp/profile-activity
```

No contribution snake is included. The previous setup referred to a nonexistent snake workflow; that stale guidance has been replaced.

See [content sources](docs/PROFILE_CONTENT.md), [project notes](docs/PROJECTS.md) and [asset conventions](assets/README.md). Keep SVG labels and README text in sync; links live outside the SVGs.
