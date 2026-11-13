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
  for a snug fit (see [Assembly](docs/ASSEMBLY.md#before-you-start)).

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

Short version — the full guide with tools, torque and checks is [`docs/ASSEMBLY.md`](docs/ASSEMBLY.md).

1. Check the bearing fits; sand the outer ring's Ø61 pocket if the RAU5005 does not go in snugly.
2. Press the printed GT2 sleeve over the outer ring's rim.
3. Slide the RAU5005 onto the inner ring's Ø50 seat from the thread side up to the Ø52 flange, then
   the spacer ring behind it (lip towards the bearing).
4. Put the inner ring with the bearing into the outer ring (bearing outer ring in the Ø61 pocket).
5. Put the clamp ring on top and tighten the six DIN 7991 M2.5×8 screws in a star pattern: snug
   (0.3–0.5 N·m), not tight. Check that it turns smoothly.
6. Screw the flattener into the clamp ring and the OAG (or the next part) onto the inner ring.
7. Fit the pulley on the motor, lay the belt over sleeve and pulley and tension it with the motor's
   slots (2–3 mm deflection mid-span). Check: turns freely, no play, belt tracks.

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
- Scripts (`docs/cnc/make_drawings.py`, `docs/label_exploded.py`, `cad/logo/make_logo.py`): GPL-3.0-or-later, see [LICENSE](LICENSE).
- Documentation text: CERN-OHL-S-2.0, as part of the hardware design.

The original rotator design in `cad/original/` is the author's own and is published under the same
hardware licence.
