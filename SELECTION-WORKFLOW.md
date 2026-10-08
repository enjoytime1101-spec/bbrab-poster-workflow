# Selection delivery v1

The customer supplies real business identity once, then selects among three finite layouts. No LLM is required. This addition is executable; the original v3 handoff compiler remains available separately.

```sh
python3 scripts/compile_selection.py examples/selection-profile.json --variant orbit --output /tmp/bbrab-selection-demo
cd renderer
npm ci
node scripts/workflow-render.mjs /tmp/bbrab-selection-demo
```

The renderer exports `poster.png` and `motion.mp4` using Remotion 4.0.534, local Noto Sans SC fonts, 1280×720 pixels and six seconds of silent restrained motion. It requires a supported Node/Chromium environment. Set `REMOTION_BROWSER_EXECUTABLE` to an installed compatible Chrome/Chromium executable, or use Remotion's documented browser installation. Runtime setup is separate from a successful render. Review the actual files before customer delivery.

Variants: `orbit` (dark technical orbit layout), `editorial` (light editorial layout), `celebration` (red celestial layout). Holidays: `space_day`, `mid_autumn`, `national_day`, `new_year`, `spring_festival`. Domain: `satellite` or `rocket`. Concept drawings are explicitly labeled; no generated technical specifications or enterprise claims.

The [platform delivery skill](skill/bbrab-aerospace-delivery/SKILL.md) documents authenticated BBRabai APIs. This public pack does not contain platform credentials, production data, user accounts, a hosting service, or the platform's private queue implementation. Installing this repository does not install those APIs. Platform readiness must be checked on the actual deployment.

Images are not model-generated. The workflow does not certify artistic suitability, infer a complete brand identity, or publish to social media. Reusing a template and selecting again consume no model tokens; compute, storage and any applicable Remotion license are separate costs.

Remotion licensing: [official terms](https://www.remotion.pro/license). Free usage eligibility depends on the actual individual/company; do not assume all enterprise users qualify. Dependencies retain their own licenses.
