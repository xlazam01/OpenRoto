"""Manufacturing drawings (PDF) for the four milled OpenRoto rings, for the JLCCNC order.

JLCCNC machines the geometry from the STEP file; threads, tolerances, roughness and finish come only
from the 2D drawing. The section profiles below are the same numbers as the SolidCraft designs in
../../cad (parameters at their release-1 values; r = radius, z measured from each part's bottom face).

    python -I docs/cnc/make_drawings.py        (writes docs/cnc/openroto_<part>.pdf)
"""
import datetime
import math
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon

OUT = os.path.dirname(os.path.abspath(__file__))
REV = "A"
DATE = datetime.date(2026, 11, 8).isoformat()
INK = "#111111"
DIM = "#0b3d91"
CL = (0, (8, 2, 1, 2))

MATERIAL = "Aluminium 6061-T6"
GENERAL = [
    "Units mm. Untoleranced sizes: ISO 2768-mK. Ø values in the half section are diameters.",
    "Geometry per the STEP file; this drawing governs threads, fits, roughness and finish.",
    "Edge chamfers as modelled (0.1-0.2 x 45°); break all other sharp edges 0.1-0.2.",
    "Surface roughness Ra 3.2 unless marked.",
    "Finish: bead blast (fine), then anodise black, matte (Type II), all over.",
    "All sizes, fits and threads apply AFTER anodising.",
]


def mirror(pts):
    return [(-r, z) for r, z in pts]


def draw_pieces(ax, pieces, both=False, lw=0.9):
    for pts in pieces:
        polys = [pts, mirror(pts)] if both else [pts]
        for poly in polys:
            ax.add_patch(Polygon(poly, closed=True, facecolor="white", edgecolor=INK, lw=lw,
                                 hatch="////", zorder=2))


def leader(ax, xy, text, xytext, ha="left"):
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=7.4, color=DIM, ha=ha, va="center",
                arrowprops=dict(arrowstyle="-|>", color=DIM, lw=0.6, shrinkA=1, shrinkB=0,
                                mutation_scale=7), zorder=5)


def vdim(ax, x, z0, z1, text, ext_from):
    for z in (z0, z1):
        ax.plot([ext_from, x], [z, z], color=DIM, lw=0.35, zorder=4)
    ax.annotate("", xy=(x, z0), xytext=(x, z1),
                arrowprops=dict(arrowstyle="<|-|>", color=DIM, lw=0.6, mutation_scale=6, shrinkA=0,
                                shrinkB=0), zorder=5)
    ax.text(x - 0.12, (z0 + z1) / 2, text, fontsize=7.4, color=DIM, va="center", ha="right",
            rotation=90, zorder=5)


def sheet(title, part, step, notes, pieces, xlim, ylim, detail, plan=None, overview_ylim=None):
    fig = plt.figure(figsize=(11.69, 8.27))  # A4 landscape
    fig.patch.set_facecolor("white")
    fr = fig.add_axes([0, 0, 1, 1]); fr.axis("off"); fr.set_xlim(0, 297); fr.set_ylim(0, 210)
    fr.add_patch(plt.Rectangle((10, 10), 277, 190, fill=False, lw=1.0, color=INK))
    fr.text(14, 196, f"{title}  —  manufacturing drawing", fontsize=12, weight="bold", color=INK, va="top")

    # title block
    tb = [("Project", "OpenRoto (rotator of Triton)"), ("Part", title), ("3D model", step),
          ("Material", MATERIAL), ("Finish", "bead blast + black anodise, matte"), ("Qty", "1"),
          ("Units", "mm, see dimensions (not to scale)"), ("Rev / date", f"{REV} / {DATE}")]
    x0, y0, w, h = 187, 10, 100, 44
    fr.add_patch(plt.Rectangle((x0, y0), w, h, fill=False, lw=0.8, color=INK))
    for i, (k, v) in enumerate(tb):
        y = y0 + h - 4.5 - i * 5.2
        fr.text(x0 + 2, y, k, fontsize=6.5, color="#555555", va="center")
        fr.text(x0 + 22, y, v, fontsize=8.5 if k == "Part" else 7.0, color=INK, va="center",
                weight="bold" if k == "Part" else "normal")

    # notes
    lines = [f"{i + 1}. {t}" for i, t in enumerate(GENERAL + notes)]
    fr.text(14, 56, "NOTES", fontsize=7.2, weight="bold", color=INK, va="top")
    for i, t in enumerate(lines):
        fr.text(14, 52 - i * 3.5, t, fontsize=6.7, color=INK, va="top")

    # detail: half section, large
    ax = fig.add_axes([0.04, 0.30, 0.66 if plan else 0.70, 0.60])
    ax.set_aspect("equal"); ax.axis("off"); ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    draw_pieces(ax, pieces)
    detail(ax)
    fr.text(14, 182, "HALF SECTION A-A  (wall only, right of the axis, enlarged; Ø = diameter)",
            fontsize=8, color=INK, weight="bold", va="top")

    # overview: full section, small
    ov = fig.add_axes([0.72, 0.62 if plan else 0.66, 0.25, 0.22])
    ov.set_aspect("equal"); ov.axis("off")
    draw_pieces(ov, pieces, both=True, lw=0.5)
    zmax = max(z for p in pieces for _, z in p)
    ov.plot([0, 0], [-3, zmax + 3], color=INK, lw=0.4, ls=CL)
    ov.set_xlim(-42, 42); ov.set_ylim(*(overview_ylim or (-6, zmax + 6)))
    ov.text(0.5, 1.0, "SECTION A-A (full, small)", transform=ov.transAxes, ha="center",
            fontsize=7, color=INK, weight="bold")

    if plan:
        ap = fig.add_axes([0.72, 0.27, 0.25, 0.33]); ap.set_aspect("equal"); ap.axis("off")
        plan(ap)
        ap.text(0.5, 1.0, "TOP VIEW (telescope side)", transform=ap.transAxes, ha="center",
                fontsize=7, color=INK, weight="bold")

    path = os.path.join(OUT, f"openroto_{part}.pdf")
    fig.savefig(path)
    plt.close(fig)
    print("wrote", path)


# ---------------------------------------------------------------- inner ring (z0 = thread end face)
INNER = [(25, 9.5), (25, 3.6), (24.9, 3.5), (23.6, 3.5), (23.6, 2.7), (23.954, 2.7), (23.954, 0),
         (22.7, 0), (22.5, 0.2), (22.5, 7.8), (24, 9.3), (24, 10.2), (24.1, 10.3), (25.9, 10.3),
         (26, 10.2), (26, 9.6), (25.9, 9.5)]


def detail_inner(ax):
    leader(ax, (26.0, 9.9), "Ø52  flange", (28.3, 11.1))
    leader(ax, (25.0, 6.5), "Ø50 h6  bearing seat (THK RAU5005), Ra 0.8 - note 7", (28.3, 7.6))
    leader(ax, (25.0, 9.45), "bearing shoulder: ⊥ 0.02 to A, Ra 1.6", (28.3, 9.6))
    leader(ax, (23.6, 3.1), "Ø47.2  thread relief, 0.8 long", (28.3, 4.4))
    leader(ax, (23.954, 1.4), "M48x0.75-6g  external, 2.7 long - note 8", (28.3, 1.6))
    leader(ax, (22.5, 4.5), "Ø45  bore (clear aperture)", (17.0, 4.5), ha="right")
    leader(ax, (24.0, 9.8), "Ø48 x 1.0 deep", (17.0, 11.3), ha="right")
    leader(ax, (23.25, 8.55), "1.5 x 45°", (17.0, 8.6), ha="right")
    leader(ax, (23.954, 0.0), "thread end face", (17.0, -0.8), ha="right")
    vdim(ax, 20.6, 0, 10.3, "10.3", ext_from=22.4)
    vdim(ax, 21.5, 0, 2.7, "2.7", ext_from=22.4)
    vdim(ax, 21.5, 3.5, 9.5, "6.0", ext_from=22.4)
    ax.text(30.5, -1.6, "A = axis of the Ø50 seat.  M48 thread coaxial to A within Ø0.05.",
            fontsize=7.2, color=DIM, ha="center")


sheet("Inner ring", "inner_ring", "cad/openroto_inner_ring.step",
      ["Ø50 h6 is the fit for the THK RAU5005 inner ring: confirm against THK catalog 382E, 'Fit', before ordering.",
       "M48x0.75 male thread (camera side) screws into the OAG; it ends at the 0.8 relief before the seat.",
       "Seat and shoulder free of burrs and anodising runs; the bearing slides onto the Ø50 seat."],
      [INNER], (8, 44), (-2.6, 12.8), detail_inner)

# ---------------------------------------------------------------- spacer ring (z0 = camera-side face)
SPACER = [(25.025, 0.1), (25.125, 0), (27.4, 0), (27.5, 0.1), (27.5, 0.9), (27.4, 1.0), (26, 1.0),
          (26, 1.4), (25.9, 1.5), (25.125, 1.5), (25.025, 1.4)]


def detail_spacer(ax):
    leader(ax, (27.5, 0.5), "Ø55", (28.6, 0.5))
    leader(ax, (26.0, 1.25), "Ø52  lip, 0.5 high (presses only on the bearing inner ring)", (28.6, 2.2))
    leader(ax, (25.025, 0.75), "Ø50.05 +0.02/0  bore\n(slides on the Ø50 seat)", (17.6, 2.4))
    leader(ax, (26.5, 0.0), "both faces flat 0.01,\nparallel 0.02, Ra 1.6", (17.6, -0.8))
    vdim(ax, 24.1, 0, 1.5, "1.5", ext_from=25.0)
    vdim(ax, 29.2, 1.0, 1.5, "0.5", ext_from=26.1)


sheet("Spacer ring", "spacer_ring", "cad/openroto_spacer_ring.step",
      ["Thin part (1.5 mm): keep it flat, no clamping marks on the faces; deburr the bore."],
      [SPACER], (17.5, 33.5), (-1.3, 2.9), detail_spacer, overview_ylim=(-4, 5.5))

# ---------------------------------------------------------------- clamp ring (z0 = bearing-side face)
# section through two of the six holes (0 and 180 deg)
CLAMP_IN = [(23.842, 3.55), (29.85, 3.55), (31.15, 2.25), (31.15, 0.2), (30.95, 0), (28.7, 0),
            (28.5, 0.2), (28.5, 1.15), (23.842, 1.15), (23.642, 1.35), (23.642, 3.35)]
CLAMP_OUT = [(35.15, 3.55), (38.8, 3.55), (39, 3.35), (39, 1.7), (38.8, 1.5), (35, 1.5), (35, 0),
             (34.05, 0), (33.85, 0.2), (33.85, 2.25)]


def detail_clamp(ax):
    ax.plot([32.5, 32.5], [-0.8, 4.4], color=INK, lw=0.4, ls=CL)
    leader(ax, (39.0, 2.6), "Ø78", (40.3, 2.6))
    leader(ax, (33.85, 1.0), "6x Ø2.7 through, csk 90° to Ø5.3,\nPCD Ø65 (top view)", (40.3, 5.0))
    leader(ax, (35.0, 0.75), "Ø70 x 1.5  spigot into the sleeve", (40.3, 0.6))
    leader(ax, (33.0, 0.0), "bearing clamping face: flat 0.02, Ra 1.6", (40.3, -1.3))
    leader(ax, (23.642, 2.35), "M48x0.75-6H  internal,\nthrough (flattener side)", (13.2, 5.0))
    leader(ax, (28.5, 0.7), "Ø57 x 1.15 deep  recess", (13.2, -1.0))
    vdim(ax, 22.2, 0, 3.55, "3.55", ext_from=23.5)
    vdim(ax, 37.0, 0, 1.5, "1.5", ext_from=35.1)


def plan_clamp(ap):
    ap.set_xlim(-44, 44); ap.set_ylim(-44, 44)
    for r, lw in ((39, 0.9), (38.8, 0.4), (23.842, 0.4), (23.642, 0.9)):
        ap.add_patch(Circle((0, 0), r, fill=False, lw=lw, color=INK))
    ap.add_patch(Circle((0, 0), 32.5, fill=False, lw=0.4, color=INK, ls=CL))
    for k in range(6):
        a = math.radians(60 * k)
        c = (32.5 * math.cos(a), 32.5 * math.sin(a))
        ap.add_patch(Circle(c, 2.65, fill=False, lw=0.8, color=INK))
        ap.add_patch(Circle(c, 1.35, fill=False, lw=0.6, color=INK))
    ap.plot([-43, 43], [0, 0], color=INK, lw=0.4, ls=CL)
    ap.plot([0, 0], [-43, 43], color=INK, lw=0.4, ls=CL)
    ap.text(-43, 1.5, "A", fontsize=7, color=INK, weight="bold")
    ap.text(41, 1.5, "A", fontsize=7, color=INK, weight="bold")
    ap.annotate("PCD Ø65\n6x 60°", xy=(32.5 * 0.5 - 2.0, 32.5 * 0.866 - 1.4), xytext=(-12, 6),
                fontsize=7, color=DIM, arrowprops=dict(arrowstyle="-|>", color=DIM, lw=0.6, mutation_scale=6))


sheet("Clamp ring", "clamp_ring", "cad/openroto_clamp_ring.step",
      ["M48x0.75 female thread takes the flattener (telescope side, top of the section).",
       "Countersinks take DIN 7991 M2.5 heads 0.25 below the top face; holes go through to the bottom face."],
      [CLAMP_IN, CLAMP_OUT], (13, 49), (-2.2, 6.0), detail_clamp, plan=plan_clamp, overview_ylim=(-4, 7.5))

# ---------------------------------------------------------------- outer ring (z0 = flange bottom face)
# section through two of the six tapped holes (0 and 180 deg); drill Ø2.1 x 4.8 + 118° point, csk Ø2.8
OUTER = [(28.7, 0), (38.743, 0), (38.943, 0.2), (38.943, 0.8), (38.743, 1.0), (35, 1.0), (35, 5.6),
         (34.8, 5.8), (33.9, 5.8), (33.55, 5.45), (33.55, 1.0), (32.5, 0.369), (31.45, 1.0),
         (31.45, 5.45), (31.1, 5.8), (30.7, 5.8), (30.5, 5.6), (30.5, 1.0), (28.7, 1.0), (28.5, 0.8),
         (28.5, 0.2)]


def detail_outer(ax):
    ax.plot([32.5, 32.5], [-0.8, 6.6], color=INK, lw=0.4, ls=CL)
    leader(ax, (38.943, 0.5), "Ø77.9  belt flange", (40.6, -1.2))
    leader(ax, (35.0, 3.3), "Ø70 0/-0.05  rim, Ra 1.6: the printed GT2\nsleeve (bore Ø69.8) is pressed on - note 9",
           (40.6, 3.0))
    leader(ax, (33.55, 3.2), "6x M2.5-6H, thread 4.5 deep min,\ndrill Ø2.1 x 4.8, csk 90° to Ø2.8,\nPCD Ø65 (top view) - note 10",
           (40.6, 6.4))
    leader(ax, (34.3, 5.8), "top face: flat 0.02, Ra 1.6", (40.6, 8.6))
    leader(ax, (30.5, 3.3), "Ø61 H7  bearing pocket (THK RAU5005\nouter ring), Ra 0.8 - note 7", (26.8, 7.4),
           ha="right")
    leader(ax, (29.6, 1.0), "pocket floor: parallel 0.02 to top face, Ra 1.6", (26.8, 0.4), ha="right")
    leader(ax, (28.5, 0.3), "Ø57  bore", (26.8, -1.0), ha="right")
    vdim(ax, 29.7, 1.0, 5.8, "4.8 ±0.03", ext_from=30.4)
    vdim(ax, 40.3, 0, 1.0, "1.0", ext_from=39.0)
    vdim(ax, 37.4, 1.0, 5.8, "4.8", ext_from=35.1)


def plan_outer(ap):
    ap.set_xlim(-44, 44); ap.set_ylim(-44, 44)
    for r, lw in ((38.943, 0.9), (35, 0.6), (30.5, 0.9), (28.5, 0.4)):
        ap.add_patch(Circle((0, 0), r, fill=False, lw=lw, color=INK))
    ap.add_patch(Circle((0, 0), 32.5, fill=False, lw=0.4, color=INK, ls=CL))
    for k in range(6):
        a = math.radians(60 * k)
        c = (32.5 * math.cos(a), 32.5 * math.sin(a))
        ap.add_patch(Circle(c, 1.4, fill=False, lw=0.8, color=INK))
        ap.add_patch(Circle(c, 1.05, fill=False, lw=0.5, color=INK))
    ap.plot([-43, 43], [0, 0], color=INK, lw=0.4, ls=CL)
    ap.plot([0, 0], [-43, 43], color=INK, lw=0.4, ls=CL)
    ap.text(-43, 1.5, "A", fontsize=7, color=INK, weight="bold")
    ap.text(41, 1.5, "A", fontsize=7, color=INK, weight="bold")
    ap.annotate("6x M2.5\nPCD Ø65, 60°", xy=(32.5 * 0.5 - 1.2, 32.5 * 0.866 - 1.0), xytext=(-12, 6),
                fontsize=7, color=DIM, arrowprops=dict(arrowstyle="-|>", color=DIM, lw=0.6, mutation_scale=6))


sheet("Outer ring", "outer_ring", "cad/openroto_outer_ring.step",
      ["Ø61 H7 (61.000-61.030): housing for the RAU5005 outer ring; hold it after anodising (THK 382E not checked).",
       "First JLCCNC build: the Ø61 pocket came out tight and was sanded until the bearing went in snugly.",
       "Rim Ø70 carries the printed PETG GT2 sleeve with a 0.2 mm press fit: round, no burrs.",
       "M2.5-6H threads usable after anodising; DIN 7991 M2.5x8 screws reach 4.5 below the top face.",
       "Pocket depth 4.8 < bearing width 5: the clamp ring presses the bearing's outer ring, not this ring."],
      [OUTER], (6, 54), (-2.0, 9.4), detail_outer, plan=plan_outer, overview_ylim=(-4, 9.5))
