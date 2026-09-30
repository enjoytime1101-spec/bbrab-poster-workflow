# BBRab Poster Workflow

[Playground](https://enjoytime1101-spec.github.io/bbrab-poster-workflow/) · [Releases](https://github.com/enjoytime1101-spec/bbrab-poster-workflow/releases) · [Skill](skill/bbrab-poster-workflow/SKILL.md) · [Prompt blocks](prompt-blocks/README.md)

A reference-first workflow for enterprise holiday posters when customers report “wrong industry” but cannot describe the desired result. Separate business facts from creative proposals, compile a reviewable production handoff, and keep acceptance tied to actual images and human judgment.

This is the standalone **workflow / Skill / prompt asset pack**, version 3.0.0, extracted and adapted from a local poster-workbench prototype. It includes a working offline brief compiler and browser preview. It does not include that prototype's private server integration, database, image renderer, generated sample images or deployment records. The version follows the source workflow; this is the first public release of this pack.

## What it does

- Compile structured briefs into deterministic, fingerprinted handoffs.
- Block incomplete real-hardware briefs without a model, evidence source and product reference.
- Distinguish rocket launch services, satellite hardware and satellite applications.
- Supply four versioned prompt cards for diagnosis, art direction, visual review and aerospace.
- Specify confirmation, actual-image review, targeted repair and designer handoff.

**It does not generate images, authenticate users, persist approval, decode reference files, bill model calls or automatically certify correctness.** The portable graph describes host responsibilities; only the compiler is executable here. No MCP server, n8n/Dify native import or production platform integration is claimed.

## Install and run

Python 3.10+; no third-party runtime dependencies, API keys or network calls. Git and Python commands below run locally.

```sh
git clone https://github.com/enjoytime1101-spec/bbrab-poster-workflow.git
cd bbrab-poster-workflow
git checkout v3.0.0
python3 -m venv .venv
.venv/bin/python skill/bbrab-poster-workflow/scripts/poster_workflow.py \
  examples/rocket-concept.json --output job.json
```

Alternatively download and extract the versioned source archive from Releases, then run the same Python command from its root. No package registry installation is required. `job.json` contains an awaiting-confirmation handoff, **not a produced or accepted poster**.

For your own brief:

```sh
.venv/bin/python skill/bbrab-poster-workflow/scripts/poster_workflow.py \
  brief.json --asset-root ./assets --output job.json
```

References are local files within the asset root. Their bytes are fingerprinted; source and rights are user declarations. The compiler deliberately reports that it has not decoded the image. A host must inspect actual images and validate file properties before production.

Exit codes: `0` complete handoff; `2` blockers reported in JSON; `1` invalid input/file. See [API and fields](skill/bbrab-poster-workflow/references/contract.md).

**Upgrade:** fetch tags, review CHANGELOG, back up your briefs, then check out the desired version. Recompile changed inputs; never reuse old confirmation with a new plan ID. Keep private assets outside this repository.

**Uninstall:** remove the downloaded checkout and optional `.venv`; remove any separately installed Skill directory. Keep customer files only according to your own retention policy. There are no background services, registry packages or server-side data created by this tool.

## Install the Skill

Copy `skill/bbrab-poster-workflow/` into your agent's supported Skills directory. It contains its own executable script and references, so it is independently usable. Follow your agent's installation instructions; this repository does not modify agent configuration automatically. The Skill invokes the compiler and requires an available authorized image tool for production.

## Workflow and architecture

Intake → visible direction selection → local compilation → human confirmation → external image/layout tool → actual-image review → accept, targeted repair, or designer handoff.

`workflow.json` is a platform-neutral specification. A host must implement authenticated ownership, persistent state, plan-bound consent, artifact validation, model execution, costs and the two-failed-review limit. [Integration](INTEGRATION.md) describes these boundaries.

Rules run locally without tokens. Only the relevant prompt card and brief should be sent to a model. No measured token reduction, first-pass acceptance rate or model-routing advantage is claimed.

## Browser Playground

The English [Playground](https://enjoytime1101-spec.github.io/bbrab-poster-workflow/) provides editable fictional inputs, copy and JSON download. It does not upload files, call a model, store data or produce a complete compiler result. Real-hardware mode remains blocked until references are supplied through the CLI.

For a local preview: `python3 -m http.server 8769 --bind 127.0.0.1 --directory docs`.

UI: 1080px content width, two columns above 680px, single-column mobile layout; system fonts, navy ink, teal actions and neutral surfaces. CSS tokens and light/dark states are in `docs/style.css`. No external fonts or images are requested.

## Validation and limitations

```sh
python3 -m unittest discover -s tests -v
node --check docs/app.js
```

CI runs Python 3.10–3.13, a fresh-venv CLI smoke test and JavaScript syntax checks. Tests cover missing evidence, path/symlink escape, explicit rights declarations, changed-reference fingerprints, dimensions and no invented approval. See [verification](VERIFICATION.md).

Prompt cards require model and customer evaluation. Human reviewers must verify hardware structure, exact copy, brand fit, actual dimensions and holiday hierarchy. No customer result is bundled. General aerospace sources are linked as conceptual reading, never as evidence for a customer's model.

## License

Apache-2.0 for this repository's original code and text; see LICENSE and NOTICE. No third-party image, font, customer asset or private platform code is bundled. See THIRD_PARTY_NOTICES.md. Brand names and external source links do not imply endorsement.
