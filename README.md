<p align="center"><img src="docs/banner.png" alt="OpenRoto" width="100%"></p>

# OpenRoto

**A slim, belt-driven camera rotator for M48 imaging trains.** A THK RAU5005 crossed roller ring
carries the camera side; a 120-tooth GT2 ring on the telescope side is driven by a 12T pulley and a
closed 340 mm belt, so 10:1. About 10.4 mm of optical length, Ø45 clear aperture.

![OpenRoto assembly](cad/openroto_assembly.png)

OpenRoto is the rotator of Triton, the author's Esprit 100ED imaging train, and belongs to the
[OpenWheel](https://github.com/xlazam01/OpenWheel) family. It has no electronics of its own: in
Triton the motor runs on [AstroUniBoard](https://github.com/xlazam01/AstroUniBoard) channel **R**.

| Document | |
|---|---|
| [Parts](docs/PARTS.md) | what each part is, its material and how to make it |
| [BOM](docs/BOM.md) | what to buy, print and mill |
| [Assembly](docs/ASSEMBLY.md) | tools, steps, belt tension, final check |
| [CNC order package](docs/cnc/) | STEP + PDF drawing per milled ring, JLCCNC settings |
| [CAD notes](cad/README.md) | design files, parameters, checks, deviations from the original |
| [Logo](cad/logo/) | badge and lockup SVGs for embossing, same style as Triton and OpenWheel |

## Specifications

| | |
|---|---|
| Interfaces | telescope side: female M48×0.75 (flattener); camera side: male M48×0.75 (OAG / next part) |
| Optical length | ~10.4 mm; overall height 13.05 mm |
| Clear aperture | Ø45 mm |
| Outside diameter | Ø78 mm (clamp ring); belt flange Ø77.9 mm |
| Bearing | THK RAU5005 crossed roller ring, 50 × 61 × 5 mm |
| Drive | 120T GT2 ring, 12T pulley, closed GT2 belt 340 mm × 6 mm, 10:1; centre distance 97.90 mm |
| Motor | 17HS08-1004S (NEMA 17 pancake), 16 µsteps → 88.889 steps/°; mounted outside the rotator |
| Homing | none on the rotator itself; Triton homes it with the AstroUniBoard IMU (gravity) |
| Materials | milled 6061-T6 rings, bead blasted and black matte anodised; printed PETG GT2 sleeve |

## Design notes

- **Slim on purpose.** The goal was a rotator with the smallest possible impact on back focus, as
  one part of the Triton train. That is why the **motor is not part of the rotator**: in Triton it is
  mounted on the OpenWheel filter wheel (the next part on the rotating side) and drives the rotator by
  the belt. The rotator itself is only the bearing, four rings and the GT2 sleeve.
- **M48 on both sides.** The design is fixed to M48×0.75, but the principle — a thin crossed roller
  ring clamped between two threaded rings, with a belt ring on the fixed side — scales to other common
  thread sizes (M54, M68, …) with a bigger bearing.
- **Fits.** The rings were milled at JLCCNC, which cannot guarantee a defined precision fit for the
  bearing. The inner ring's seat was fine as delivered; the outer ring's bearing pocket had to be sanded
  for a snug fit (see [Assembly](docs/ASSEMBLY.md#before-you-start-checks-on-the-parts)).

## How it works

```
 telescope / flattener  (M48 male)
        │
  ┌─────┴─────┐  clamp ring             ─┐
  │  bearing  │  outer ring + GT2 sleeve │ fixed: screwed to the flattener,
  │  RAU5005  │                         ─┘ the belt runs on the sleeve
  │           │  inner ring             ─┐
  └─────┬─────┘  spacer ring             │ rotating: carries the OAG, filter wheel,
        │                               ─┘ camera and the motor
   OAG / camera  (M48 female)
```

- **Fixed side** (telescope): the clamp ring screws onto the flattener. Six M2.5 countersunk screws
  pull it onto the milled outer ring and clamp the bearing's outer ring between them. A thin printed
  GT2 sleeve is pressed over the outer ring's rim and sits on its belt flange.
- **Rotating side** (camera): the bearing's inner ring sits on the inner ring's Ø50 seat under its
  Ø52 flange. The spacer ring below it is clamped by the next part of the train when that is screwed
  onto the inner ring's M48 thread.
- **Drive:** the motor rides on the rotating side and walks its 12T pulley around the fixed 120T
  sleeve with a closed belt. The motor mount is slotted for belt tension.

## Getting the parts

| What | Where | Documents |
|---|---|---|
| Inner, spacer, clamp and outer ring | CNC, e.g. JLCCNC: 6061-T6, bead blast + black anodise | [`docs/cnc/`](docs/cnc/) — order guide, STEP + PDF drawing per part |
| GT2 sleeve | 3D print, PETG, no supports | [`cad/openroto_gt2_sleeve.3mf`](cad/openroto_gt2_sleeve.3mf), print notes in [`docs/PARTS.md`](docs/PARTS.md) |
| Bearing, screws, pulley, belt, motor | buy | [`docs/BOM.md`](docs/BOM.md) |

## Assembly

Short version — the full guide with the part checks, tools, torque and the access rules is
[`docs/ASSEMBLY.md`](docs/ASSEMBLY.md).

1. Check the parts: bearing fits (sand the outer ring's Ø61 pocket if needed), sleeve height ≤ 6.5 mm,
   screw length (M2.5×6 if an ×8 bottoms in the tapped hole), flattener thread ≤ 2.7 mm into the clamp ring.
2. Press the printed GT2 sleeve fully onto the outer ring's rim and flange.
3. Bearing into the outer ring's pocket (press its outer race with the clamp ring), inner ring into the
   bearing from the top, spacer ring onto the seat from below (raised lip towards the bearing).
4. Clamp ring on, six DIN 7991 M2.5 screws in opposite pairs, snug (0.3–0.5 N·m). Check: a gap between
   clamp plate and sleeve, and the inner ring turns smoothly.
5. Screw the camera-side part (OAG) onto the inner ring **before** the flattener, holding the inner ring
   by its bore.
6. Screw the rotator onto the flattener holding the clamp ring — never turn the train by the camera.
7. Pulley height by dry fit, belt on, tension with the motor plate's slots. Route the cables, then
   check: no play, belt tracks, back to the mark after ±360°.

## Repository

| Folder | Content |
|---|---|
| [`cad/`](cad/) | SolidCraft designs (editable source), STEP and 3MF exports, the original STEP in `cad/original/` |
| [`docs/`](docs/) | parts, BOM, assembly guide, exploded view and the CNC order package |
| `hw/`, `fw/`, `sw/` | empty: no electronics; the drive runs on AstroUniBoard |
| [`release/`](release/) | release packages (none yet) |

The `.sc` files open in SolidCraft; everyone else uses the STEP exports.

## Status

- 2026-11-08: release-1 rebuild of the original rotator (the author's own earlier design,
  [`cad/original/`](cad/original/)) in SolidCraft, parts checked (no feature warnings, closed meshes).
- Built once for Triton. The rings came from JLCCNC; the outer ring's bearing pocket was sanded
  for a snug fit.
- 2026-11-13: outer ring (milled, with the belt flange and six tapped M2.5 holes) and GT2 sleeve
  (printed, 0.2 mm press fit on the rim) split into two designs as in the original; outer-ring drawing added.
- **Open:** the 12T pulley model is a typical envelope until the real part is measured.

## License

- Hardware design files (`cad/`, the drawings and the exploded view in `docs/`): CERN-OHL-S-2.0, see
  [LICENSE-HARDWARE](LICENSE-HARDWARE).
- Scripts (`docs/cnc/make_drawings.py`, `docs/label_exploded.py`, `docs/make_section.py`, `cad/logo/make_logo.py`): GPL-3.0-or-later, see [LICENSE](LICENSE).
- Documentation text: CERN-OHL-S-2.0, as part of the hardware design.

The original rotator design in `cad/original/` is the author's own and is published under the same
hardware licence.
