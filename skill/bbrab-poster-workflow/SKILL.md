---
name: bbrab-poster-workflow
description: Turn unclear enterprise holiday-poster feedback into a reference-backed brief, production handoff and human review, with separate rocket, satellite hardware and satellite-services paths.
---

# Enterprise poster workflow

Use the customer's language for their content. Packaged instructions are English.

1. Establish industry, concrete business and holiday. Treat “wrong industry” as reported feedback, not a diagnosis. When the customer cannot name a desired result, offer three visibly different directions with their tradeoffs; ask them to select, combine or reject. Do not invent their preference.
2. Separate confirmed facts, source-backed references and proposed creative choices. Collect brand, channel, exact copy, dimensions, industry cues, prohibited elements and a chosen direction. Read [the contract](references/contract.md) for JSON fields.
3. For aerospace, read [aerospace rules](references/aerospace.md). Distinguish launch services, satellite hardware and satellite applications. Real hardware requires a named model, evidence source and a rights-declared product reference. Otherwise offer an explicitly labeled concept.
4. Run the bundled tool: `python3 scripts/poster_workflow.py brief.json --asset-root ./assets --output job.json` (paths relative to this Skill directory). Resolve blockers. The compiler fingerprints reference bytes but does not decode them or authenticate rights. Inspect actual images before treating them as valid references.
5. Present the brief and plan ID for customer confirmation. The tool stops at awaiting_customer_confirmation; it cannot record consent or launch a model. A hosting platform must bind consent and output to that plan ID and authenticated owner. Any input or reference change requires recompilation and renewed confirmation.
6. Use an available, authorized image tool for backgrounds/concepts. Preserve exact product images, logos and text with compositing/layout. If no image tool is connected, deliver the handoff explicitly as pending production. JSON, wireframes and prompts are not finished posters.
7. Review the actual rendered image against the confirmed brief and references. Unknown structure or unreadable text remains unknown. Do not let a model's self-score stand in for customer acceptance. Record artifact hash, plan ID, reviewer, explicit checks and corrective notes. Two failed reviews trigger designer handoff; the host must persist and enforce this count.

Prompt cards: [prompt assets](references/prompts.json). Load only the needed card. Use local checks for fixed requirements; send only relevant brief fields and assets to a model. Repair the rejected region while preserving accepted decisions. Record every generation attempt and human time; no token-saving percentage is claimed.
