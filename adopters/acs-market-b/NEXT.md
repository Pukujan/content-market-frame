# ACS B — next-session handoff (read this, not the chat)

**State:** product-introduction marketing site **NOT generated or deployed**. **Owning issue:** [ABA #65](https://github.com/Pukujan/app-builder-automation/issues/65). **Workflow correction:** [ABA #67](https://github.com/Pukujan/app-builder-automation/issues/67) and [routing PR #68](https://github.com/Pukujan/app-builder-automation/pull/68).

**Owner directions accepted:** individual multi-agent project builder (D3); intended attention returned to *real project work* (D6); product must be introduced immediately, then problem→mechanism→proof→technical detail (D7). Evidence is product-source-backed; no observed customer outcome or ROI claim.

**Unresolved:** Q3 main CTA action was specifically **not selected**. Do not invent an installer, preview, documentation button, or side effect. Exact hero/creative acceptance and launch approval remain separate.

**RIGHT builder path:** [real ABA adopter generator](https://github.com/Pukujan/app-builder-automation/blob/main/server/src/loop.mjs) (same mechanism used for IRE React site); **NOT** the internal Dyad/Pro `eval/run-dyad-pro.mjs` track. [Full Dyad preflight PR #66](https://github.com/Pukujan/app-builder-automation/pull/66) and [manual HTML PR #64](https://github.com/Pukujan/app-builder-automation/pull/64) are CLOSED UNMERGED. Neither is an ACS B solution or prerequisite.

**Inputs:** [SPEC.md](SPEC.md) and [run.mjs](run.mjs) in this directory. They invoke **ABA's real `generate()`**, adapting only the consumer data-access instructions without modifying ABA. Read [source-pinned Experience Brief](../../examples/acs-version-b.experience.draft.json) for deeper story, only if needed.

**Do now from a working local environment with existing ABA checkout and owner gateway:**

```sh
node adopters/acs-market-b/run.mjs --aba /path/to/app-builder-automation --out /path/to/isolated-acs-b --inspect
node adopters/acs-market-b/run.mjs --aba /path/to/app-builder-automation --out /path/to/isolated-acs-b --execute
```

The runner refuses to overwrite an output directory. It generates **only a non-public React review candidate**. After the run, inspect `ACS_B_ABA_RECEIPT.json`, actual app, and desktop/mobile screenshots. Get human design judgment and clarify Q3 before release. **No deployment is authorized.**

**Context budget:** read this file, the current ABA #65 issue and SPEC. Do not load the whole project history or repeat closed capability audits. If generated output exists locally, inspect it before regenerating. If provider access is unavailable, record the exact problem on #65 and leave task open.
