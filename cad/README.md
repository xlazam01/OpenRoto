# cad

SolidCraft designs (`.sc`, the editable source), STEP exports and 3MF meshes. All parts are modelled
in their assembly position: optical axis = Z, telescope side +Z, bearing seat from z = 0 to 5. The
assembly links every part with `component.insert_design`, so it needs no mates.

`original/top_assy_rotator.step` is the original model this release-1 rebuild was measured from (moved
here from Triton). The Solid Edge `Rotator` folder is only a placeholder and was not used.

## Own parts

| Design | Make | Notes |
|---|---|---|
| `openroto_inner_ring` | milled Al, black matte anodised | rotating side: Ø45 bore with 1.5 × 45° lead-in under a Ø48 counterbore, Ø50 bearing seat, Ø52 × 0.8 flange over the bearing, male M48×0.75 (Ø47.908, 2.7 long) with a Ø47.2 undercut |
| `openroto_spacer_ring` | milled Al, black matte anodised | Ø50.05 / Ø55 × 1.5 under the bearing inner ring, Ø52 × 0.5 lip; turns with the inner ring |
| `openroto_clamp_ring` | milled Al, black matte anodised | fixed side: Ø78 × 3.55, female M48×0.75 (minor Ø47.284), Ø57 recess over the inner-ring flange, Ø70 × 1.5 spigot into the sleeve, 6 × Ø2.7 countersunk 90° to Ø5.3 on Ø65 |
| `openroto_gt2_sleeve` | **two parts in reality** (see below) | bearing housing Ø61, 120T GT2 ring (tip Ø75.886 = 120·2/π − 2·0.254), Ø77.886 × 1 belt flange, 6 × Ø2.0755 pilot holes 4.8 deep on Ø65 for the M2.5 screws |
| `openroto_assembly` | — | all parts, 6 screws, pulley at (0, 97.900) and the belt |

**Outer ring + GT2 sleeve:** `openroto_gt2_sleeve` merges what the real rotator has as two parts:
a milled aluminium outer ring (Ø61 bearing pocket, six tapped M2.5 holes, rim) and a thin printed GT2
sleeve pressed over the rim. The rebuild joined the original's two bodies by mistake (the original
STEP has them as `outter ring` and `GT2 Pulley`). Its STEP and 3MF are reference geometry until the
design is split; the six "pilot holes" stand for the tapped M2.5 holes.

Threads are plain cylinders at the thread diameters of the original (cosmetic), as in the STEP.

Deviations from the original STEP, all small:
- clamp holes: a plain 90° countersink to Ø5.3 at the face instead of Ø5.1 + 0.1 mm cylinder (same cone);
- sleeve: one body instead of the original's outer ring + GT2 pulley (wrong, see above); the 0.2 mm V-notch between the core
  top and the tooth ring is filled; the pilot holes have a flat bottom instead of a 118° drill point
  (that cone tip gave an open mesh edge) and a 0.2 × 90° countersink instead of a chamfer;
- GT2 grooves: standard approximation (R0.555 tooth arc, 0.75 deep, R0.15 lip), not a copy of the
  original tooth form. The sleeve comes out 0.24 % heavier than the original's sleeve bodies.

## Bought parts (linked designs)

| Design | Part | Source of the dimensions |
|---|---|---|
| `openroto_bearing_rau5005` | THK RAU5005 crossed roller ring, 50 × 61 × 5, 0.2 chamfers (envelope) | the original STEP |
| `openroto_screw_din7991_m2.5x8` | DIN 7991 M2.5×8 hex socket countersunk, A2 (×6), head 0.25 below the clamp face | dk 4.8, 90° head, hex socket s1.5 × 0.8 deep: fastener listings for DIN 7991 M2.5 (bolts.co.uk, Spalding Fasteners); the standard text was not checked |
| `openroto_pulley_gt2_12t` | GT2 12T pulley, 5 mm bore, 6 mm belt (envelope: Ø11 flanges, Ø10 × 6 hub toward the motor) | **typical, not from a datasheet** — measure the bought pulley and correct `flange_d`, `hub_d`, `hub_l` |
| `openroto_belt_gt2_340` | GT2 closed belt 340 mm, 6 mm wide (smooth band from the pulley tips to the backing, 0.63 thick) | GT2 pitch geometry |

Centre distance for the 340 mm belt on 120T/12T, solved exactly: **97.900 mm** (pitch radii
38.197 / 3.820 mm, wrap 221.1° / 138.9°). The motor mount (OpenWheel Triton variant, slotted plate) sets
the centre distance between 93.8 and 98.7 mm, so the belt is tensioned by sliding the motor.
The pulley sits on +Y in the assembly; its real direction comes from the OpenWheel motor mount (Triton #6).

## Parameters

Every size is a parameter of its design (the points of the revolved profile sketches are expressions,
dof 0). Main ones: inner ring `bore_d`, `bear_bore`, `bear_w`, `thr_d`, `thr_len`; clamp `cl_od`,
`cl_t`, `thr_d`, `hole_pcd`, `hole_d`, `cs_d`, `n_holes`; sleeve `bear_od`, `sl_od`, `fl_od`,
`belt_h`, `pilot_d`, `hole_pcd`, `teeth`, `groove_r`, `groove_depth`, `lip_r`.

Limits:
- The sleeve's 240 groove-lip fillets (`GrooveLipFillets`, R0.15) are picked at fixed points for
  120 teeth: changing `teeth` needs that feature redone. A full sleeve rebuild took about 40 min
  in SolidCraft 0.29 and 2.4 min after the 2026-11-08 update (the fillets ~77 s, the pilot holes
  ~110 s). Opening the file is instant (saved model).

## Checks (2026-11-08, re-checked 2026-11-09)

| Design | Volume mm³ (original STEP) | Feature warnings | Mesh (`meshcheck`) | Print (`printcheck --up=+z`) |
|---|---|---|---|---|
| inner ring | 2977.7 (2977.4) | none | 0 open edges | — (milled) |
| spacer ring | 482.4 (482.4) | none | 0 open edges | — (milled) |
| clamp ring | 8220.3 (8221.0) | none | 0 open edges | — (milled) |
| GT2 sleeve | 10365.2 (10340.4) | none | 0 open edges | no supports, no thin walls, bed contact 2127 mm² (flange down) |
| bearing | 4780.9 (4780.5) | none | — | — |

All designs open from their saved model (`solidcraft-cli bench-open`: `adopted: true, recomputed: 0`).
A SolidCraft update (2026-11-08 evening) stopped loading the saved models of older files, so every
design was re-saved on 2026-11-09 (`bench-open <file> --save <out>` recomputes and saves, but saves no
model when a feature fails, so check its output). The update also lost two chamfer picks, both
reselected with the volume unchanged and 0 open edges: the clamp's `HoleChamfers` (at +Y of each hole,
8220.3) and the sleeve's `ToothRingInnerChamfer` (at 45° on the Ø70 top edge, 10365.2; print check
unchanged). The assembly links all designs with no feature warnings.
The clamp follows `hole_pcd` and `cl_od` without errors (`check_parameters`).

Kernel notes from the build: a revolved hole cutter and a 120-cylinder groove cut both logged
"Boolean retry", so the sleeve's tooth ring is one planar sketch extrude (tip circle, inner circle,
120 patterned groove circles half a pitch off the revolve seam) joined to a revolved flange/core that
overlaps it, and the clamp's holes are `solid.hole` countersinks.

## Print settings (GT2 sleeve)

For the thin printed sleeve (once split from the outer ring): flange on the bed, no supports. PETG, 0.2 mm layers, at least 3 perimeters so the teeth are solid.
