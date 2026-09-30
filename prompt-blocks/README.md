# Prompt blocks

The canonical cards are [prompts.json](../skill/bbrab-poster-workflow/references/prompts.json).

| Card | Purpose | When to load |
| --- | --- | --- |
| poster.diagnose | Evidence-based rejection diagnosis | The customer says the image is wrong but cannot define a target |
| poster.art-direction | Distinct visual proposals | Business facts are known; preference is not |
| poster.visual-review | Located findings and targeted repairs | An actual image and confirmed plan are available |
| poster.aerospace | Reference-first space-industry constraints | Rocket, satellite hardware or application work |

Cards contain inputs, acceptance criteria, a failure example and fallback. They are versioned proposals, not universally validated prompts. No provider/model benchmark is claimed. Read only the relevant card; do not resend the full library each turn. Do not include credentials or unrelated conversation history in model input.

For evaluation record prompt version, model/version, actual image and reference identifiers, customer verdict, defects, all failed generation costs and human minutes. Compare the same tasks with the same reviewers before making quality or savings claims.
