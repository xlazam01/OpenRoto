# JLCCNC order — OpenRoto rings

Everything needed to order the four milled rings of OpenRoto (release 1) from
[JLCCNC](https://jlccnc.com) (JLCPCB's CNC service). The printed GT2 sleeve and the bought parts are
not part of this order — see [`../BOM.md`](../BOM.md).

JLCCNC machines the shape from the **STEP** file. Threads, tolerances, surface roughness and finish
are made **only from the 2D drawing** (PDF), so every part needs both files. Untoleranced sizes follow
ISO 2768-m. ([CNC Machining Order Guidelines](https://jlccnc.com/help/article/cnc-machining-ordering-guidelines))

## Files per part

| Part | Upload: 3D | Upload: 2D drawing | Threads |
|---|---|---|---|
| Inner ring | [`cad/openroto_inner_ring.step`](../../cad/openroto_inner_ring.step) | [`openroto_inner_ring.pdf`](openroto_inner_ring.pdf) | 1 × M48×0.75-6g external |
| Spacer ring | [`cad/openroto_spacer_ring.step`](../../cad/openroto_spacer_ring.step) | [`openroto_spacer_ring.pdf`](openroto_spacer_ring.pdf) | none |
| Clamp ring | [`cad/openroto_clamp_ring.step`](../../cad/openroto_clamp_ring.step) | [`openroto_clamp_ring.pdf`](openroto_clamp_ring.pdf) | 1 × M48×0.75-6H internal |
| Outer ring | [`cad/openroto_outer_ring.step`](../../cad/openroto_outer_ring.step) | [`openroto_outer_ring.pdf`](openroto_outer_ring.pdf) | 6 × M2.5-6H, 4.5 deep min |

The STEP files are exported from the SolidCraft designs and are the release-1 geometry. The M48
threads are modelled as plain cylinders (thread diameters), the M2.5 holes as the Ø2.1 tap drill;
the drawing calls them out.

## Settings on the quote page (same for all four)

| Option | Choose | Why |
|---|---|---|
| Process | CNC machining (turning/milling) | round parts, one setup per side |
| Material | **Aluminium 6061-T6** | standard, anodises well |
| Surface finish | **Anodizing with bead blasting**, colour **black** | matte black; anodising alone is not blasted ([order guide](https://jlccnc.com/help/article/cnc-machining-ordering-guidelines)) |
| Threads | **Yes** — inner ring 1, clamp ring 1, outer ring 6 (M2.5), spacer none | add the remark below; M48×0.75 is a fine-pitch thread |
| Tightest tolerance | ±0.01–0.02 mm (only the features marked on the drawing) | Ø50 h6 seat, Ø61 H7 pocket, Ø50.05 spacer bore, flatness/parallelism notes |
| Surface roughness | Ra 0.8 (marked faces), Ra 3.2 elsewhere | bearing seat Ra 0.8, contact faces Ra 1.6 |
| 2D drawing | upload the PDF | required for threads and tolerances |
| Quantity | 1 (2 if you want a spare set) | |

Remark to paste into the order (per part, threads on inner, clamp and outer ring):

> Thread M48x0.75 (fine pitch, 6g external / 6H internal), full profile as shown on the PDF. Sizes,
> fits and threads apply after anodising (bead blast + black anodise, matte). Please keep the Ø50 h6
> bearing seat and the flatness/parallelism notes on the drawing.

Outer ring:

> 6x M2.5-6H tapped holes, 4.5 mm full thread minimum, as shown on the PDF. Sizes, fits and threads
> apply after anodising (bead blast + black anodise, matte). The Ø61 H7 bearing pocket must take a
> 61 mm bearing outer ring by hand: please do not make it tight.

## Critical features (check on delivery)

| Part | Feature | Spec | How to check |
|---|---|---|---|
| Inner ring | bearing seat | Ø50 h6 (49.984–50.000) | micrometer; the RAU5005 slides on without play |
| Inner ring | external thread | M48×0.75-6g, 2.7 long | screws into the OAG / any M48 T-ring by hand |
| Inner ring | bearing shoulder | ⊥ 0.02 to the seat axis | bearing sits flat |
| Spacer ring | bore | Ø50.05 +0.02/0 | slides onto the inner ring seat |
| Spacer ring | faces | flat 0.01, parallel 0.02 | on a surface plate |
| Clamp ring | internal thread | M48×0.75-6H through | flattener screws in by hand |
| Clamp ring | bottom face | flat 0.02 | clamps the bearing outer ring evenly |
| Clamp ring | 6 × countersinks | Ø2.7 / 90° to Ø5.3 on PCD 65 | DIN 7991 M2.5 heads sit 0.25 below the face |
| Outer ring | bearing pocket | Ø61 H7 (61.000–61.030), 4.8 ±0.03 deep | the RAU5005 goes in by hand, snugly; sand evenly if tight |
| Outer ring | rim | Ø70 0/−0.05 | the printed sleeve presses on |
| Outer ring | 6 × M2.5 | 6H, 4.5 deep min, PCD 65 | a DIN 7991 M2.5×8 screws in by hand through the clamp ring |

## Open before ordering

- **Bearing fits:** JLCCNC cannot hold a defined precision fit reliably. On the first build the inner
  ring's Ø50 seat was fine as delivered, but the outer ring's Ø61 pocket was too tight and had to be
  sanded for a snug fit of the RAU5005. THK lists the fits in catalog 382E ("Fit"), which was not checked.
- Wall at the thread relief is 1.1 mm (Ø47.2 relief vs Ø45 bore) — fine for 6061, but don't let the
  quote engineer thin it further.

## Regenerating the drawings

The PDFs come from [`make_drawings.py`](make_drawings.py) (matplotlib). The section profiles in it
are the numbers of the SolidCraft designs at their release-1 parameters; change both together.

    python -I docs/cnc/make_drawings.py
