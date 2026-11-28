<div align="center">

<img src="assets/portfolio/repo-card.svg" width="520" alt="safe-to-send-21-series-map bespoke project visual">

**SAFE TO SEND · GOVERNED AI ENGINEERING SERIES · SAFE TO SEND 21 SERIES MAP**

[GitHub Profile](https://github.com/sghatge) · [Portfolio](https://sghatge.github.io/adobe-campaign-v8-governance/)

</div>

---

# safe-to-send-21 · The Series Map

![Safe to Send, Episode 21](docs/episode.png)

**Safe to Send · Episode 21** — Week 3 retrospective of a 28-day learn-in-public series on governing AI in CRM operations.

> Three weeks, twenty-one repos, one idea: in CRM, AI needs guardrails, tests and shared standards before it needs more autonomy.

This repo is the index for the whole series. **Start with [SERIES.md](SERIES.md)**: every episode, its repo, and a diagram of which episode builds on which.

## Why a map repo

Twenty-eight small repos are easy to start and hard to navigate. One registry file (`registry.json`) is the single source of truth. `build_map.py` validates it (every episode present, no episode depending on a later one, repo names match numbers) and regenerates `SERIES.md` with a Mermaid dependency diagram GitHub renders on its own.

## Run it

```bash
python build_map.py
```

```
SERIES.md written: 28 episodes, 15 build on an earlier one
```

## The three ideas the series keeps coming back to

1. **Gate the action, not the prompt.** Episodes 01–07, 13 and 16.
2. **Rules decide, models explain, tests prove it.** Episodes 08–12.
3. **Standardise before you automate.** Episodes 15, 17, 18 and 20.

MIT · [Sangram Ghatge](https://www.linkedin.com/in/sangram-g-2369705b) · #SafeToSend


---

## Portfolio integration & safe use

This repository is part of the **Safe to Send** 28-episode engineering series on governed AI for CRM and marketing operations.

- [Series index and episode map](https://github.com/sghatge/safe-to-send-21-series-map)
- [Complete portfolio](https://github.com/sghatge/sghatge)
- [OPSFORGE Build Lab](https://sghatge.streamlit.app/) — portfolio overview; this repository remains independently usable without the Build Lab.

**Safe-use boundary:** use the supplied examples and synthetic data for evaluation. Review the implementation, dependencies and tests before adapting it. Do not connect it to a production CRM, customer dataset or activation endpoint without a separate security, privacy and change-control review. No production integration or deployment is implied by this repository.
