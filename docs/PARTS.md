# Parts

What each part of OpenRoto does, what it is made of and how to get it. Numbers match the
[exploded view](openroto_exploded.png) and the [BOM](BOM.md). Dimensions and checks are in
[`../cad/README.md`](../cad/README.md); masses are computed from the CAD volumes.

![OpenRoto exploded view](openroto_exploded.png)

The rotator has two halves. The **fixed side** (clamp ring, outer ring with the GT2 sleeve, the bearing's outer ring)
screws onto the telescope's flattener. The **rotating side** (inner ring, spacer ring, the bearing's
inner ring) carries everything behind it: OAG, filter wheel, camera, and the motor that drives it all.

## 1 — Inner ring (rotating side)

The bearing journal and the camera-side thread. A Ø45 bore (1.5 × 45° lead-in under a Ø48
counterbore), a Ø50 h6 seat for the bearing's inner ring under a Ø52 × 0.8 flange, and a male
M48×0.75 thread (2.7 mm long, Ø47.2 relief) for the OAG or the next part of the train.

- Material: aluminium 6061-T6, bead blasted and black matte anodised. ~8 g.
- Make: CNC turning; order with [`cnc/`](cnc/) (STEP + PDF drawing, the drawing carries the thread and
  the h6 fit). Check the seat with a micrometer on delivery.

## 2 — Spacer ring (rotating side)

A thin washer (Ø50.05 / Ø55 × 1.5 with a Ø52 × 0.5 lip) under the bearing's inner ring. When the next
part is screwed onto the inner ring's M48 thread, it presses on the spacer, and the spacer clamps the
bearing's inner ring against the inner ring's flange.

- Material: aluminium 6061-T6, bead blasted and black matte anodised. ~1.3 g.
- Make: CNC turning (same order as the other rings). Faces flat 0.01, parallel 0.02.

## 3 — Clamp ring (fixed side)

The telescope-side interface and the bearing's outer clamp. Ø78 × 3.55 with a female M48×0.75 thread
for the flattener, a Ø57 recess over the inner ring's flange, a Ø70 × 1.5 spigot that centres it in the
GT2 sleeve above the outer ring's rim, and six Ø2.7 holes countersunk 90° on a Ø65 circle.

- Material: aluminium 6061-T6, bead blasted and black matte anodised. ~22 g.
- Make: CNC turning + drilling; order with [`cnc/`](cnc/). Bottom face flat 0.02.

## 4 — Outer ring + GT2 sleeve (fixed side)

**4a — Outer ring (milled).** The bearing housing: a Ø61 pocket 4.8 deep for the bearing's outer ring
(its top face stays 0.2 below the bearing, so the clamp ring presses on the bearing), a Ø57 lip under
it, six M2.5 holes tapped through on a Ø65 circle for the clamp-ring screws, the Ø70 rim the GT2 sleeve is
pressed onto, and the Ø77.9 × 1 belt flange the sleeve sits on.

- Material: aluminium 6061-T6, bead blasted and black matte anodised. ~18 g.
- Make: CNC turning + drilling and tapping; order with [`cnc/`](cnc/) (STEP + PDF drawing, the drawing
  carries the threads and the pocket fit).
- **Bearing fit:** JLCCNC cannot guarantee a defined precision fit. On the first build the Ø61 pocket
  came out too tight and was sanded until the RAU5005 sat in it snugly; the inner ring's Ø50 seat was
  fine as delivered. Expect to fit the pocket by hand, or order it from a shop that holds the tolerance.

**4b — GT2 sleeve (printed).** A thin printed ring carrying the 120 GT2 teeth (tip Ø75.9, 6.3 high:
0.2 mm below the clamp plate, so the clamp ring rests on the bearing only).
Its Ø69.8 bore is pressed over the outer ring's Ø70 rim and held by friction; the clamp ring's spigot
goes into its top.

- Material: PETG (stiff, little creep). ~5 g.
- Make: [`../cad/openroto_gt2_sleeve.3mf`](../cad/openroto_gt2_sleeve.3mf), either face down, no supports,
  0.2 mm layers, at least 3 perimeters so the teeth are solid. Try the fit on the rim before assembly:
  if it is loose or cracks, change `sl_id` in the design (or the slicer's hole compensation).

## 5 — Crossed roller ring THK RAU5005 (bought)

50 × 61 × 5 mm crossed roller bearing: carries axial, radial and tilting loads in one thin ring, so
the camera cannot sag or wobble. Its outer ring is clamped between the outer ring and the clamp ring (fixed), its
inner ring between the inner ring's flange and the spacer (rotating). ~38 g.

## 6 — Screws DIN 7991 M2.5×8, ×6 (bought)

Hex socket countersunk screws, A2 stainless, 1.5 mm key. They screw into the tapped holes of the outer ring and
clamp the bearing's outer ring; the heads sit 0.25 mm below the clamp face.

## 7 — GT2 pulley 12T (bought)

12-tooth GT2 pulley for a 6 mm belt, 5 mm bore, fixed to the motor shaft with its grub screws. The
CAD model is a typical envelope, not a datasheet part.

## 8 — GT2 belt 340 mm (bought)

Closed GT2 belt, 340 mm (170 teeth), 6 mm wide. 120T : 12T gives 10:1. Centre distance 97.900 mm
(pitch radii 38.197 / 3.820 mm, wrap 221.1° on the sleeve).

## 9 — Stepper motor 17HS08-1004S (bought, not drawn)

NEMA 17 pancake stepper, 1.0 A, 5 mm shaft. It rides on the rotating side and walks its pulley around
the fixed sleeve. At 16 microsteps: 200 · 16 · 10 = 32 000 steps per turn of the camera, 88.889 steps/°.
The motor mount is not part of this repo (see [BOM](BOM.md#not-in-this-bom)).
