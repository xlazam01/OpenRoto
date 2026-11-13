# OpenRoto logo

The camera sensor — a 3:2 frame around the optical axis — turned inside the rotator ring. The ring is a
rotation arrow, and the light leaves the sensor and breaks out through the top of the ring as an arrow.
Same drawing rules as the Triton and OpenWheel logos: ring Ø20/Ø17.2, 0.7 mm knockouts, 1.1 mm lines,
the light-path arrowhead like the trident's centre tine, with its tip at the same height (11.4 mm).

| File | What |
|---|---|
| `openroto_badge.svg` | Badge only, 20 × 21.4 mm (ring Ø20) |
| `openroto_lockup.svg` | Badge + "OPENROTO" (Arial Bold, 6 mm caps), 68.6 × 21.4 mm |
| `make_logo.py` | Generator (shapely + matplotlib): `python -I make_logo.py` rewrites the SVGs and `preview.png` |
| `preview.png` | Both, light on black anodised aluminium |

The SVGs hold only filled closed outlines in mm (no strokes, no text objects).

## Embossing in SolidCraft

1. Sketch on the face (`project_edges: false`): `sketch.insert_svg {path, at: [x, y], align: "center", width: <mm>, angle}`,
   then `sketch.constraint.fix` on all its points (dof 0).
2. Extrude **join** or **cut** 0.6 mm for a two-colour print, 0.4 mm for a single-colour relief. The
   default profile pick ("all") takes the sensor frame's opening as a hole.

The badge has 3 islands (ring with the arrowhead, sensor frame with the beam, axis dot); area 114.8 mm²
at ×1, so an extrude is 114.8 mm² × depth.

## Where it is used

Nowhere yet: the rotator's parts are milled and anodised. Candidates are a laser-marked clamp ring face
or the printed GT2 sleeve's flange.

## Size limits (0.4 mm nozzle)

At the drawn size, lines are 1.1 mm wide or more and gaps at least 0.7 mm. Only the two arrow tips are thinner.
- Badge: no smaller than Ø16 mm.
- Lockup: no smaller than 55 mm wide.
