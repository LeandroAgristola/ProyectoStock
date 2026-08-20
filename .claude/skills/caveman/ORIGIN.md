# Origin

This skill is vendored from the Caveman project.

- Upstream: https://github.com/JuliusBrussee/caveman
- Path upstream: `skills/caveman/`
- Commit: `a42ef766cedef6160407418a359a52939b2d20b9`
- Version: 2.2.0
- License: MIT (see `LICENSE`)
- Author: Julius Brussee

Only the standalone `caveman` skill is vendored here — no binaries, hooks, or
MCP servers from upstream. To update, copy `skills/caveman/SKILL.md` and
`README.md` from a newer upstream commit and refresh this file.

Upstream also ships the full plugin (hooks, statusline badge, extra skills like
`caveman-commit` / `caveman-review` / `caveman-stats`), installable with:

```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
```
