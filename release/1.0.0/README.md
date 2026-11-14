# OpenRoto 1.0.0

First release of the OpenRoto camera rotator: a flat, belt-driven M48 rotator built around a THK
RAU5005 crossed roller ring. **10.05 mm of optical length**, Ø45 clear aperture, 10:1 belt drive.
Build it with the [assembly guide](../../docs/ASSEMBLY.md) and the [bill of materials](../../docs/BOM.md).

| Part | Version |
|---|---|
| Mechanics | release 1 (`cad/`, SolidCraft) |
| Milled rings | rev B drawings (outer ring: M2.5 holes tapped through) |
| GT2 sleeve | 6.3 mm high, bore Ø69.8 |
| Electronics | none — the motor runs on any stepper driver; in Triton on [AstroUniBoard](https://github.com/xlazam01/AstroUniBoard) channel R |

## Status

Built once and running on the author's Esprit 100ED (Triton imaging train) since 13 November 2026.

> **Two things to know before ordering.** The Ø61 bearing pocket of the outer ring needed sanding on
> the first build — JLCCNC does not hold a defined precision fit, so expect to fit it by hand (see
> [Assembly, before you start](../../docs/ASSEMBLY.md#before-you-start-checks-on-the-parts)).
> The **12T pulley model is a typical envelope, not a measured part**: it is in the assembly STEP for
> context only. Measure the pulley you buy before relying on the CAD around it.

## Contents

| Folder | Files |
|---|---|
| `cad/cnc/` | the four milled rings (inner, spacer, clamp, outer): STEP for the shape and PDF drawing for threads, tolerances and finish. A CNC service needs **both** files per part |
| `cad/printed/` | GT2 sleeve: 3MF for printing (flange down, no supports), STEP for editing |
| `cad/assembly/` | the complete assembly as STEP, including the bought parts for context |
| `bom/mechanical.csv` | everything to buy, print and mill, with search terms |
| `SHA256SUMS` | checksums of all files above (`sha256sum -c SHA256SUMS`) |

## Ordering the rings (CNC)

Material 6061-T6, bead blast + **black matte anodise**, ISO 2768-m for untoleranced sizes. Threads and
the marked fits come from the PDF drawing only, so upload the STEP **and** the PDF for each part.
Full order guide, the JLCCNC option list and the remark to paste into the order:
[`docs/cnc/README.md`](../../docs/cnc/README.md).

Threads: inner ring 1 × M48×0.75-6g external, clamp ring 1 × M48×0.75-6H internal, outer ring
6 × M2.5-6H tapped through, spacer none.

Check on delivery: Ø50 h6 seat on the inner ring, Ø61 H7 pocket in the outer ring, Ø70 0/−0.05 rim,
and that both M48 threads run together by hand.

## Printing the sleeve

PETG, 0.2 mm layers, at least 3 perimeters, flange down (+Z), no supports. Checked in that
orientation: 6.30 mm high, 570 mm² bed contact, no overhangs needing support, no walls below the
nozzle diameter. It is a 0.2 mm press fit on the outer ring's Ø70 rim — press it on evenly, for
example with a flat board on a table.

## Verification

Every file in this package was checked before release:

| Check | Result |
|---|---|
| STEP, OpenCASCADE (`stepcheck.py`) | all 6 solids BRepCheck valid, 0 badly meshed faces at 0.01 deflection |
| Mesh, 3MF (`meshcheck.py`) | 0 open / non-manifold edges |
| Printability (`printcheck.py --up +z`) | sleeve: 0 overhangs needing support, 0 thin walls |
| Volumes vs the design | inner 2977.7, spacer 482.4, clamp 8220.3, outer 6509.0, sleeve 3843.0 mm³ |

## Licence

Hardware and CAD under [CERN-OHL-S v2](../../LICENSE-HARDWARE); the repository's scripts and docs under
[GPL-3.0](../../LICENSE).
