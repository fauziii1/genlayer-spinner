# GenLayer Layered Orbit Spinner

An original animated loading spinner concept for the GenLayer Portal.

## Deliverables
- `genlayer-spinner.svg` — self-contained animated SVG.
- `genlayer-spinner.css` — dependency-free CSS spinner.
- `preview.html` — preview on light and dark backgrounds.
- `design-notes.md` — design rationale and implementation notes.

## Design
The Layered Orbit concept combines a compact GenLayer-inspired layered G mark with an orbiting gradient ring and a subtle pulsing node. The animation uses a smooth 1.55 second infinite loop and is designed to remain recognizable at small sizes.

## Accessibility
The animation respects `prefers-reduced-motion: reduce`. The HTML example uses `role="status"` and an accessible loading label.

## Performance
No JavaScript, external fonts, images, or runtime dependencies are required.