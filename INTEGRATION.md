# Host integration

Load workflow.json as a specification and implement its nodes in your orchestrator. It is not an executable cloud workflow or native import file.

1. Authenticate ownership server-side. Never accept an owner or reviewer identifier solely from untrusted JSON.
2. Validate user input, resolve authorized references locally, and call compile_brief. The CLI itself has no authentication and should not be exposed directly to arbitrary network callers.
3. Inspect reference content with a real image decoder and check access rights. Fingerprints prove byte identity, not licensing, technical correctness or safety.
4. Present the exact job and capture explicit customer consent bound to plan_id. Store a revision number. Changing any brief or reference invalidates confirmation.
5. Run the host's authorized generation/editing and layout service. Preserve hardware photos and exact text through compositing. No supplier adapter or paid route is enabled by this pack.
6. Decode the actual output, verify dimensions/format, bind its SHA-256 to plan_id and record provider/version plus trusted usage records. Reject stale callbacks and duplicate charge attempts.
7. Collect all six ordinary or eleven aerospace checks as explicit human decisions. Unknown cannot pass; failed file checks cannot be overridden by an overall approval. Record reviewer and timestamp. Enforce two failures → designer handoff in durable host state.

Do not use client-submitted cost fields for billing. Include failed calls and manual work in later cost analysis. Automatic retries require host idempotency and budgets. Customer references and output must remain private unless the customer authorizes publication.

The compiler embeds brief data into a prompt as JSON; downstream models must treat it as untrusted task data. This boundary is an instruction, not a proven prompt-injection defense.
