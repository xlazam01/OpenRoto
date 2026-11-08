# OpenRoto

A flat camera rotator for M48 imaging trains: a THK RAU5005 crossed-roller ring between a
fixed clamp ring (female M48×0.75 to the flattener) and a rotating inner ring (male M48×0.75 to the
next part of the train). A printed 120-tooth GT2 sleeve on the fixed side is driven by a 12T pulley
and a 360 mm closed belt from a NEMA17 on the rotating side, so 10:1.

OpenRoto is the rotator of [Triton](../Triton/) (Esprit 100ED imaging train) and belongs to the
OpenWheel naming family. It has no electronics of its own: in Triton the motor runs on AstroUniBoard
channel **R** (88.889 steps/° at 16 µsteps, IMU homing).

![OpenRoto assembly](cad/openroto_assembly.png)

| | |
|---|---|
| Optical length | ~10.4 mm (flattener M48 face to the inner ring's M48 shoulder); overall 13.05 mm |
| Clear aperture | Ø45 mm |
| Bearing | THK RAU5005 crossed roller ring, 50 × 61 × 5 mm |
| Drive | 120T GT2 sleeve, 12T pulley, 360 mm closed GT2 belt (6 mm), 10:1; centre distance 108.51 mm |
| Motor | 17HS08-1004S (mount on the OpenWheel motor box in Triton) |
| Materials | milled aluminium rings; printed GT2 sleeve (PETG) |

## Parts

Sources are SolidCraft designs in [`cad/`](cad/), with STEP exports and 3MF meshes next to them.
Details, parameters and checks: [`cad/README.md`](cad/README.md). Bill of materials:
[`docs/BOM.md`](docs/BOM.md).

## Status

- 2026-11-08: repository created; parametric SolidCraft rebuild of the original STEP
  (`cad/_ref/top_assy_rotator.step`) with all parts and the bought parts linked into
  `cad/openroto_assembly.sc`. Not built yet.
