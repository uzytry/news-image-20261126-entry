# News Image — 26 November 2026

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/uzytry/news-image-20261126-entry/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/uzytry/news-image-20261126-entry/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Entry for the make.fun bounty
[news-image-20261126](https://make.fun/competitions/news-image-20261126):
sum up 26 November's world news in one image.

The entry is a one-page newspaper front page for Thursday 26 November 2026:
US tariffs on 14 trading partners, a drone attack in Kuwait, a missile strike
on a Kyiv shopping mall, the Hormuz tanker mine claim, and continuing strikes
in Gaza — plus a bottom strip on the Ebola outbreak in DR Congo, the Macy's
Thanksgiving Day Parade postponed by a storm, and a new ECB chief.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
pre-built image `entry.png` (1024x1024) byte for byte to
`/output/entry.png`, then verifies with SHA-256 that the copy is identical.
The run is fully deterministic: two runs produce byte-identical output.

## Run

```sh
python3 main.py
# Wrote /output/entry.png (940180 bytes, sha256 034fe2e70c9abe3f96e2bf5e9e22832220565247ac4bdcbe550c5eeb46c69754)
```

## License

MIT — see [LICENSE](LICENSE).
