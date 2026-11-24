# octo-feather-realcase

Standing private test repo for [octo-feather](https://github.com/0xTomDaniel/octo-feather).

What it is for:

- Real-case runs: kit lanes run real `gh` merges, issue reads and closes, and post-merge routines here, against real GitHub, to prove a fix with no stand-ins.
- Recording capture: the real `gh` answers from those runs are saved unmodified as the kit's testkit recordings (`tests/gate/kit/testkit/recordings/`), so the kit's tests replay real tapes.

No gate depends on this repo: the kit's tests replay the recordings, never this repo.

Each lane prefixes its branches with its lane key (for example `gh1249-`) and names its issues and PRs after the lane, so concurrent lanes stay out of each other's way.
