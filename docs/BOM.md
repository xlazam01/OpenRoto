# BOM

One OpenRoto (release 1). Item numbers match the [exploded view](openroto_exploded.png) and
[`PARTS.md`](PARTS.md). Own parts are in [`../cad/`](../cad/); the rings are ordered with the
[CNC order package](cnc/).

| # | Qty | Part | Specification | Source / search term | Notes |
|---|---|---|---|---|---|
| 1 | 1 | Inner ring | 6061-T6, bead blasted + black matte anodised; male M48×0.75-6g; Ø50 h6 bearing seat | CNC service (e.g. JLCCNC): [`openroto_inner_ring.step`](../cad/openroto_inner_ring.step) + [PDF](cnc/openroto_inner_ring.pdf) | rotating side, camera side thread |
| 2 | 1 | Spacer ring | 6061-T6, bead blasted + black matte anodised; Ø50.05 / Ø55 × 1.5 | CNC service: [`openroto_spacer_ring.step`](../cad/openroto_spacer_ring.step) + [PDF](cnc/openroto_spacer_ring.pdf) | under the bearing inner ring |
| 3 | 1 | Clamp ring | 6061-T6, bead blasted + black matte anodised; female M48×0.75-6H; Ø78 × 3.55 | CNC service: [`openroto_clamp_ring.step`](../cad/openroto_clamp_ring.step) + [PDF](cnc/openroto_clamp_ring.pdf) | fixed side, telescope side thread |
| 4a | 1 | Outer ring | 6061-T6, bead blasted + black matte anodised; Ø61 bearing pocket, 6 × M2.5 tapped on Ø65, rim for the sleeve | CNC service — **no separate STEP yet**, see note | the Ø61 pocket needed sanding for a snug bearing fit |
| 4b | 1 | GT2 sleeve, 120T | thin printed ring, 120 GT2 teeth + belt flange; PETG, 0.2 mm layers, ≥ 3 perimeters | print flange down, no supports — **no separate 3MF yet**, see note | pressed over the outer ring's rim |
| 5 | 1 | Crossed roller ring | THK RAU5005, 50 × 61 × 5 mm | THK distributors; search "THK RAU5005" | the only precision bought part |
| 6 | 6 | Countersunk screw | DIN 7991 (ISO 10642) M2.5×8, hex socket 1.5 mm, A2 stainless | fastener shops; search "DIN 7991 M2.5x8 A2" | into the outer ring's tapped holes |
| 7 | 1 | GT2 pulley, 12T | 5 mm bore, for 6 mm belt, with grub screws | 3D-printer parts shops; search "GT2 12T pulley 5mm bore 6mm" | model is a typical envelope; measure yours (see [`../cad/README.md`](../cad/README.md)) |
| 8 | 1 | GT2 closed belt | 340 mm (170 teeth), 6 mm wide | 3D-printer parts shops; search "GT2 closed loop belt 340mm 6mm" | not 360 mm: centre distance 97.90 mm |
| 9 | 1 | Stepper motor | 17HS08-1004S, NEMA 17 pancake, 1.0 A, 5 mm shaft | StepperOnline; search "17HS08-1004S" | 16 µsteps → 88.889 steps/° at 10:1 |

**Note on 4a/4b:** the CAD (`openroto_gt2_sleeve`) draws the outer ring and the GT2 sleeve as one
printed body; the real rotator has a milled outer ring and a thin printed sleeve. Until the model is
split, `openroto_gt2_sleeve.step`/`.3mf` are reference geometry only, not order or print files. See
[`PARTS.md`](PARTS.md#4--outer-ring--gt2-sleeve-fixed-side).

## Not in this BOM

- **Motor mount** (housing + slotted plate for belt tension): the Triton variant of
  [OpenWheel](https://github.com/xlazam01/OpenWheel) (`cad/triton/`), with its own screws. Any mount that
  holds the motor on the camera (rotating) side at a 93.8–98.7 mm adjustable centre distance works.
- **Driver electronics**: any stepper driver; in Triton the motor runs on
  [AstroUniBoard](https://github.com/xlazam01/AstroUniBoard) channel R.
- **Adapters** to your telescope and camera: OpenRoto has M48×0.75 on both sides (female towards the
  telescope, male towards the camera).
