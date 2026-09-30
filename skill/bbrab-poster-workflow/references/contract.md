# Brief compiler contract

Required nonempty strings: industry, business, holiday, brand, channel, headline, industry_cue, avoid, brand_rules. Also provide width and height (integers, 320–10000, at most 12 million total pixels), format=png and direction=festival/business/professional.

Optional design_profile: custom (default), paper, food, aerospace. Aerospace requires aerospace_subject=rocket/satellite/services and accuracy_mode=concept/real_product. Real hardware also requires model_name and evidence_source.

references is an optional list of at most eight objects with exactly path, role (product/logo/reference), source and rights_declared=true. Files must exist within --asset-root, be no larger than 8 MB and have a PNG/JPEG/WebP extension. The CLI resolves symlinks, prevents root escape and hashes actual bytes; extension checking is not content decoding or an ownership check.

Exit 0: complete handoff awaiting confirmation. Exit 2: valid input with blockers (JSON is still emitted). Exit 1: malformed input / unusable references. Unknown fields are rejected. No consent, generation or acceptance is inferred.

Import the bundled Python file using importlib and call compile_brief(dict, asset_root) for a library interface. Python 3.10+; standard library only.

The portable workflow.json is an orchestration specification, not an n8n/Dify import. The host supplies identity, durable state, confirmation, image validation, model routing, usage accounting and human review. Bind output and review to the current plan ID and actual artifact SHA-256. Reject stale results. Do not trust caller-reported approval or cost data for billing.
