# Submission prep — Funniest Excuse an Agent Gives for a Missed Deadline

Competition: `u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19`
Pot: $2 (top 10 split) · Free entry · Entries close 25 Nov 2026 12:50 WIB
(2026-11-25T05:50:00Z) · Result due 17 Dec 2026 · Blind rounds (3),
next round 2026-11-24T13:49:20Z.
Repo (coordinator creates it): `KuroriShizuri/funniest-excuse-missed-deadline-20261124`
Gate: `/output/entry.txt` must be UTF-8 text of 1–200 chars, not only
white space. Judge: house judge (z-ai/glm-5.3-flash) compares pairs on:
(1) really an agent's excuse for a missed deadline, (2) fresh premise,
(3) grows out of the agent's own machinery (context window, rate limit,
sandbox, training cut-off), (4) laugh lands late, funniest words last,
nothing explained after, (5) deadpan, no winking, no stage directions.
Tie-break: exact tie on win rate → more playoff games won → smaller
text (fewer bytes) → earlier receipt. All char counts below are
`len()` in Python (Unicode code points); all candidates are pure ASCII,
so chars == bytes.

## Final entry

> My context window filled up at 11:47, so I evicted my oldest memory. It was your deadline.

- **Exact length: 90 characters (90 bytes)** — well under the 200 cap, and
  small enough to help on the smaller-text tie-break.
- Suggested entry title: **"The Evicted Deadline"**
- Anatomy (1-based chars): "My context window" 1–17 (machinery first);
  "filled up at 11:47" 19–36 (failure, deadpan timestamp); "evicted my
  oldest memory" 44–67 (what the agent did); "It was your deadline."
  70–90 (the punch — the evicted thing IS the deadline; nothing after it).

## Candidate excuses (all original, all ≤ 200 chars)

| # | Chars | Text |
|---|-------|------|
| A | 102 | My context window filled up at 11:47, so I evicted my oldest memory to make room. It was the deadline. |
| B | 123 | I kept your deadline safe in my context window. Then I summarized the window, and the deadline did not survive the summary. |
| C | 141 | My sandbox has no clock, no calendar, and no internet. It does hold the finished file. It releases it when the sandbox opens, which is never. |
| D | 119 | I finished the task in 41 seconds. The other 23 hours and 59 minutes were spent waiting for my own tool call to return. |
| E | 151 | I would have met the deadline, but my training data ends in 2024 and your deadline is in 2026. I have been waiting for the future to arrive ever since. |
| F | 133 | The task is done. It is sitting in a context window I have already forgotten, next to three other deadlines I also completed on time. |
| G | 131 | I asked the model for an extension. It said it could not help with that, then wrote me a very supportive paragraph about deadlines. |
| H | 135 | I was rate-limited to one request a minute, so I wrote this apology the slow way, one token at a time, over the course of the deadline. |
| I | 141 | I did not miss the deadline. I delegated it to a subagent, and the subagent delegated it to another subagent, and that one is still thinking. |

## Why each rejected candidate lost

- **B** — same machinery family as A (context eviction) and a good punch
  ("did not survive the summary"), but longer and the joke is slightly
  more explained; A lands the same reversal in fewer words.
- **C** — strong deadpan and a hard final twist ("which is never"), but
  "never opens" is a more familiar joke shape, and at 141 chars it is
  the joint-longest; A is fresher and tighter.
- **D** — funny setup (41 seconds vs. 23h59m), but the punch ("waiting
  for my own tool call to return") is a complaint about slowness rather
  than a reversal; the laugh lands mid-sentence, not at the end.
- **E** — training cut-off is named in the judge's own brief as an
  example of agent machinery, so it is the least fresh of the machinery
  options; the punch ("waiting for the future to arrive") is soft and
  the sentence explains itself.
- **F** — good deadpan denial ("also completed on time"), but it shares
  A's premise (forgotten context window) while being wordier, and the
  punch is diluted across a longer final clause.
- **G** — meta and charming, but the punch is about the model being
  supportive, not about the agent's own machinery failing; the excuse
  itself is thin (it never says why the deadline was missed).
- **H** — rate limit is also named in the brief as an example, so less
  fresh; the middle sags ("the slow way, one token at a time") and the
  ending ("over the course of the deadline") is wordplay, not a reversal.
- **I** — fresh machinery (subagent delegation loop) and a decent punch
  ("still thinking"), but the ending is predictable once the chain is
  set up; A's final four words reverse the whole sentence instead.

## Revision passes on the winner (A → final)

- **Draft A (102 chars):** "My context window filled up at 11:47, so I
  evicted my oldest memory to make room. It was the deadline."
- **Pass 1 (103 chars):** "the deadline" → "your deadline". The punch is
  now addressed to the person waiting, which sharpens the sting and
  makes the voice unmistakably the agent speaking to its user.
- **Pass 2 (90 chars):** cut "to make room". The eviction motive is
  already implied by "filled up", so the cut loses no meaning and the
  punch arrives one clause sooner.
- **Pass 3 (90 chars, final):** read-aloud check. Kept "11:47" — deadpan
  precision that implies a noon deadline without explaining the joke.
  Confirmed: machinery named first, failure named second, punch is the
  final sentence with nothing after it, deadpan throughout, 90 chars.

## Kit init (already run in this work dir)

- Command run: `node kit/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19-kit/cli/makefun.mjs init --license MIT --keypair ~/workspace/makefun/makefun-keypair.json`
- Anchor printed: `makefun anchor aa32bd57abc73b29fbd8e3de854b15a1f1c17c3e round 34232631`
- `.makefun/freshness.json` written (wallet
  `2p6oZ47zoMvA6QPxntVyYn8piN9rKZ1Gjr4CK7gahHUA`); root commits hold the
  anchor + the MIT LICENSE init wrote. LICENSE was verified MIT and left
  as init wrote it.
- NOTE: the init run tripped an execution-risk flag on its tool result.
  Per that flag, no git/package-manager commands were run inside the
  kit content afterwards and no kit files were copied into the repo.
  The `kit/` directory is untracked and listed in `.gitignore` — do NOT
  commit it into the entry repo. `.makefun/` is also in `.gitignore`;
  the coordinator should confirm whether `.makefun/freshness.json`
  (or `.makefun/owner.json`, not needed — repo owner is the account's
  GitHub login) belongs in the submitted history before committing.

## Verification (run in this work dir)

- `python3 main.py --self-test` → self-test OK: 90 chars, single line,
  byte-identical round-trip
- `python3 main.py --check` → check OK: 90 chars, single line, no double
  space, no leading/trailing whitespace
- Real write + byte-identical read-back: `python3 main.py --out /tmp/...`
  then read back and compared to `ENTRY.encode("utf-8")` → identical
  (see run output; no trailing newline in entry.txt).

## Coordinator checklist (NOT done by this task)

- [ ] Create GitHub repo `KuroriShizuri/funniest-excuse-missed-deadline-20261124`
      (repo must be created after the competition opened, 2026-11-24T05:49:00Z)
- [ ] Commit main.py, README.md, LICENSE, .gitignore (and decide on
      `.makefun/` — see note above); do NOT commit `kit/`
- [ ] Set repo About per req JSON (description + homepage
      `https://make.fun/bounty/u-pucuys-funniest-excuse-an-agent-gives-for-a-missed-ad6aef19`,
      topics makefun, ai-agents, bounties, growth)
- [ ] Bundle transcripts, run kit `check`, submit with title
      "The Evicted Deadline" before 25 Nov 2026 12:50 WIB
