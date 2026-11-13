"""Half cross-section of OpenRoto at the clamp ring, marking the double contact of the clamp ring.

The profiles are the ones of docs/cnc/make_drawings.py (each in its part's own frame) moved to the
assembly frame of cad/openroto_assembly.sc (optical axis Z, telescope side up, bearing z 0..5).
Sleeve, bearing and belt are envelopes from the CAD (no teeth, no rollers).

    python -I docs/make_section.py      -> docs/section_clamp_contact.png
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon as Poly, FancyArrowPatch

class md:  # section profiles (r, z) copied from docs/cnc/make_drawings.py — keep in step with it
    INNER = [(25, 9.5), (25, 3.6), (24.9, 3.5), (23.6, 3.5), (23.6, 2.7), (23.954, 2.7), (23.954, 0),
             (22.7, 0), (22.5, 0.2), (22.5, 7.8), (24, 9.3), (24, 10.2), (24.1, 10.3), (25.9, 10.3),
             (26, 10.2), (26, 9.6), (25.9, 9.5)]
    SPACER = [(25.025, 0.1), (25.125, 0), (27.4, 0), (27.5, 0.1), (27.5, 0.9), (27.4, 1.0), (26, 1.0),
              (26, 1.4), (25.9, 1.5), (25.125, 1.5), (25.025, 1.4)]
    CLAMP_IN = [(23.842, 3.55), (29.85, 3.55), (31.15, 2.25), (31.15, 0.2), (30.95, 0), (28.7, 0),
                (28.5, 0.2), (28.5, 1.15), (23.842, 1.15), (23.642, 1.35), (23.642, 3.35)]
    CLAMP_OUT = [(35.15, 3.55), (38.8, 3.55), (39, 3.35), (39, 1.7), (38.8, 1.5), (35, 1.5), (35, 0),
                 (34.05, 0), (33.85, 0.2), (33.85, 2.25)]
    OUTER = [(28.7, 0), (38.743, 0), (38.943, 0.2), (38.943, 0.8), (38.743, 1.0), (35, 1.0), (35, 5.6),
             (34.8, 5.8), (33.9, 5.8), (33.55, 5.45), (33.55, 1.0), (32.5, 0.369), (31.45, 1.0),
             (31.45, 5.45), (31.1, 5.8), (30.7, 5.8), (30.5, 5.6), (30.5, 1.0), (28.7, 1.0), (28.5, 0.8),
             (28.5, 0.2)]


OUT = Path(__file__).resolve().parent / "section_clamp_contact.png"


def moved(pts, dz):
    return [(r, z + dz) for r, z in pts]


# part frames -> assembly z (from the assembly's bounding boxes)
parts = [
    ("Inner ring 1", moved(md.INNER, -4.5), "#3a3c42"),
    ("Spacer ring 2", moved(md.SPACER, -1.5), "#5a5d66"),
    ("Clamp ring 3", moved(md.CLAMP_IN, 5.0), "#2b2c30"),
    ("", moved(md.CLAMP_OUT, 5.0), "#2b2c30"),
    ("Outer ring 4a", moved(md.OUTER, -1.0), "#4a4d55"),
    ("GT2 sleeve 4b (printed)", [(34.9, 0), (37.943, 0), (37.943, 6.5), (34.9, 6.5)], "#2f6db5"),
    ("Bearing RAU5005", [(25.2, 0), (30.3, 0), (30.5, 0.2), (30.5, 4.8), (30.3, 5), (25.2, 5),
                         (25, 4.8), (25, 0.2)], "#b9bcc2"),
    ("Belt", [(37.943, 0.25), (38.573, 0.25), (38.573, 6.25), (37.943, 6.25)], "#141414"),
]

fig, ax = plt.subplots(figsize=(12, 5.6))
for name, pts, col in parts:
    ax.add_patch(Poly(pts, closed=True, fc=col, ec="k", lw=0.6, alpha=0.95))
# bearing races split line (outer race / inner race), for orientation only
ax.plot([27.75, 27.75], [0, 5], color="#777", lw=0.6, ls="--")
ax.text(26.4, 2.5, "inner\nrace", ha="center", va="center", fontsize=8)
ax.text(29.1, 2.5, "outer\nrace", ha="center", va="center", fontsize=8)
# screw axis
ax.plot([32.5, 32.5], [-1.5, 9.5], color="#999", lw=0.6, ls="-.")
ax.text(32.5, 9.6, "screw axis Ø65", ha="center", fontsize=8, color="#555")

red = "#d32f2f"
# contact A: clamp spigot face on the bearing outer race, z = 5.0 (intended)
ax.plot([28.5, 30.5], [5.0, 5.0], color="#2e7d32", lw=4, solid_capstyle="butt")
# contact B: clamp plate underside on the sleeve top, z = 6.5 (unintended)
ax.plot([35.0, 37.943], [6.5, 6.5], color=red, lw=4, solid_capstyle="butt")

ax.annotate("A  z 5.00 — clamp spigot on the bearing's outer race\n(the intended clamping face)",
            xy=(29.5, 5.0), xytext=(12.5, 9.0), fontsize=10, color="#2e7d32", va="bottom",
            arrowprops=dict(arrowstyle="->", color="#2e7d32", lw=1.4))
ax.annotate("B  z 6.50 — clamp plate on the top of the printed sleeve\n"
            "(sleeve 6.50 high on the flange at z 0): ZERO clearance",
            xy=(36.5, 6.5), xytext=(36.0, 9.0), fontsize=10, color=red, va="bottom",
            arrowprops=dict(arrowstyle="->", color=red, lw=1.4))
ax.text(39.6, 4.4,
        "Both faces touch at nominal size.\n"
        "Sleeve printed +0.05 mm, or not pressed fully\n"
        "onto the flange → the clamp rests on the PETG (B),\n"
        "lifts off the bearing (A): outer race not clamped,\n"
        "and the PETG creeps under the screw load.\n\n"
        "Fix: sleeve 6.3 high (0.2 mm gap at B);\n"
        "until then measure it ≤ 6.5 and check that a\n"
        "paper slip passes at B after tightening.",
        fontsize=9.5, va="top", color="#222",
        bbox=dict(fc="#fff4f4", ec=red, lw=1))
ax.annotate("0.2 gap", xy=(34.4, 4.9), xytext=(32.5, 2.6), ha="center", fontsize=7.5, color="#333",
            arrowprops=dict(arrowstyle="->", color="#333", lw=0.6))

labels = [("Inner ring 1", (20.4, 1.5)), ("Spacer ring 2", (26.3, -2.3)), ("Clamp ring 3", (26.6, 7.55)),
          ("Outer ring 4a", (33.9, -2.3)), ("GT2 sleeve 4b", (36.4, 3.3)), ("Bearing 5", (27.75, 4.3)),
          ("Belt 8", (38.26, 3.2))]
for t, (x, y) in labels:
    ax.text(x, y, t, ha="center", va="center", fontsize=8.5 if not t.startswith("Belt") else 7,
            color="white" if t.startswith(("Clamp", "GT2", "Belt")) else "#111",
            rotation=90 if t.startswith(("GT2", "Belt")) else 0)

ax.axhline(0, color="#bbb", lw=0.4)
ax.set_xlim(12, 52); ax.set_ylim(-3.0, 11.6)
ax.set_aspect("equal")
ax.set_xlabel("radius from the optical axis (mm)"); ax.set_ylabel("z (mm), telescope side up")
ax.set_title("OpenRoto half section through a clamp screw — clamp ring meets bearing AND sleeve", fontsize=12)
ax.grid(True, lw=0.25, color="#ddd")
fig.tight_layout()
fig.savefig(OUT, dpi=130)
print(OUT)
