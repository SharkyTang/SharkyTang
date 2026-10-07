# Profile content sources

Audited on 2026-10-07. Profile baseline: `0f4e97f`, `SharkyTang/SharkyTang`.

## Audit

The workspace root was an empty Git repository. The actual profile was cloned into `SharkyTang/`, then work began on `codex/sharky-os-profile`. The latest remote README was used, rather than an older local copy.

Existing `profile-terminal.svg`, `profile-terminal-mobile.svg` and `wechat-badge.svg` are preserved. No workflow was present. The old `SETUP.md` referred to an absent snake workflow.

## Provenance

| Content | Evidence | Decision |
| --- | --- | --- |
| Sharky / Shaoqi Tang, Computer Science, Durham University | Existing README, GitHub public profile, supplied brief | Retained |
| Final year, independent projects, Affective HCI | Supplied prompt and plan | Used as user-stated current focus; no job availability claim |
| LinkedIn, email, WeChat | Existing profile README | Retained exactly |
| Portfolio URL | Live `https://sharkytang.com/` and `/projects`, HTTP 200 | Public entry points |
| Sharky's Room | Published portfolio and local `sharkys-room/package.json` | 3D portfolio; TypeScript, React, Next.js, Three.js, GSAP, Supabase confirmed |
| ROLUNE | Published portfolio, localized project copy, `Monopoly3D` README and Creator manifest | WeChat board-game prototype; Cocos Creator and TypeScript shown |
| FOLDORA | Latest local `刀板图网站/README.md` and manifest; remote baseline also checked | Current asset editor used; public portfolio and remote baseline still describe earlier packaging focus |
| JavaScript, Python, Git, VS Code, Obsidian, Codex | Existing README; public portfolio also lists JavaScript/Python | Retained as tools used, without proficiency scores |
| Konva, IndexedDB | Current FOLDORA manifest and README | Added |
| Contribution graph | GitHub GraphQL `user.contributionsCollection.contributionCalendar` | Actual daily counts for latest 26 calendar weeks |

Java, C++, FastAPI, Docker, invented language percentages and follower/repository counts were omitted. The earlier smaller projects were superseded in this showcase by the three projects selected in the brief; their code and repositories were not changed.

## Images

- **Room:** Existing publicly published snowy-night room cover, from the portfolio's public media endpoint. Actual room screenshot.
- **ROLUNE:** Existing publicly published cover, cropped to the circular brand artwork. Labelled artwork rather than a gameplay screenshot.
- **FOLDORA:** Local `docs/verification/asset-instance-editor.png`. Actual editor screenshot with a development sample asset.

Sources were cropped and compressed deterministically. No AI-generated product screenshots were created. Images are embedded in self-contained SVGs, without external fonts, hotlinked images, scripts or `foreignObject`.

## Remaining items

- Replace ROLUNE artwork with a real gameplay screenshot.
- Add public playable/hosted links for ROLUNE and FOLDORA when they exist.
- Keep final-year status current after the academic year changes.
- Run the activity workflow after publication and inspect its first scheduled run.

Scope: README, profile artwork, setup/content documentation and a small contribution-refresh workflow. Existing assets are preserved. Contribution snake is deferred.
