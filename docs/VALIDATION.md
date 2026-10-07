# Validation — SHARKY.OS

Checked on 2026-10-07 against profile baseline `0f4e97f`.

## Rendering and layout

- The GitHub Markdown API successfully rendered the README and retained all eight image modules, `<picture>` sources, details sections and navigation links.
- The rendered HTML was reviewed locally in Chrome, with local image paths and GitHub-style Markdown layout. GitHub's `user-content-` anchor prefix was normalized only in this preview.
- Viewports: **1440, 1024, 768, 700, 414, 390 and 320 px**. All images loaded. Document scroll width matched viewport width at every size, including when both text-details sections were expanded.
- Mobile sources were selected at 700 px and below. The identity panels stack, project cards become portrait cards and the contribution graph splits into two 13-week rows.
- All 16 new SVGs passed browser checks for text staying within their viewBox. Desktop and mobile dark previews were inspected visually; a mobile light-theme preview was also captured.
- All 19 SVGs, including the three preserved original assets, parsed as XML. No scripts, event handlers, `foreignObject` or external SVG image references were found.
- Each README image has meaningful alt text, and key identity, project and technology information remains available as normal text.
- Main text, muted text, blue links and green status text were checked against both panel backgrounds. All measured contrast ratios exceed 7:1; status is also written as `ONLINE`.

This section records GitHub's Markdown output and local browser layout before publication. Inspection of the updated live profile is performed separately during publication.

## Content, links and performance

- Relative files and project-note anchors resolve. The five section anchors have matching targets after GitHub's normal prefixing.
- GitHub profile and the portfolio's home/project pages returned HTTP 200. Both reused public cover endpoints returned HTTP 200.
- LinkedIn returned HTTP 999 to automated access. Its exact existing profile URL was retained; automated checks could not independently confirm the destination. Email and WeChat were retained from the existing README.
- Project descriptions and displayed technologies were reconciled with source manifests, READMEs, current local documentation and publicly published project content.
- ROLUNE artwork is explicitly labelled artwork; FOLDORA's editor screenshot is explicitly labelled as containing a sample asset.
- Only one contribution component is used. No invented follower counts, repository counts, language percentages, proficiency ratings or job-availability claims were added.
- Desktop SVG payload: **374,323 bytes**. Mobile SVG payload: **373,971 bytes**. These totals include all eight modules selected for each layout; no external image widgets or web fonts are needed.

## Contribution update and workflow

- Every generated contribution cell was matched to the actual GitHub API response: **179 days**, **108 contributions**, from **2026-04-12 through 2026-10-07**.
- Negative counts, boolean counts, broken date sequences and GraphQL errors were rejected.
- An API-error response was passed through the command-line entry point; it exited with failure while preserving the existing chart.
- Workflow YAML parsed successfully. Default permissions are `contents: read`; only the refresh job receives `contents: write`. The official checkout Action is pinned to a verified 40-character commit SHA.
- The workflow runs on a daily schedule or manual dispatch, checks out the default branch and stages only its two generated SVGs. It uses the built-in GitHub token, with no personal token in source.
- At initial validation, the scheduled workflow had not been run on GitHub. Its first hosted execution is checked as part of publication.
- No contribution snake or package dependency was added.

## Repository checks

- `git diff --check` passed.
- Original `profile-terminal.svg`, `profile-terminal-mobile.svg` and `wechat-badge.svg` are unchanged relative to the baseline.
- No unrelated project code was changed. A credential-pattern scan found no embedded access tokens or private keys in profile source/artwork/documentation.
- These implementation checks were completed locally on `codex/sharky-os-profile` before publication.
