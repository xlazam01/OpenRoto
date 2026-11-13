"""OpenRoto logo for embossing on printed parts (same style as the Triton and OpenWheel logos).

Badge: the camera sensor (a 3:2 frame around the optical axis) turned in the rotator ring; the ring is a
rotation arrow, and the light path leaves the sensor and breaks out through the top of the ring as in
the sibling logos. The dot in the frame is the optical axis.
Geometry is in mm for a 20 mm badge; every line is >= 1.0 mm and every gap >= 0.7 mm,
so it embosses cleanly with a 0.4 mm nozzle down to ~16 mm (scale up freely).

    python -I make_logo.py            -> openroto_badge.svg, openroto_lockup.svg, preview.png

The SVGs hold filled closed outlines only (no strokes, no text), ready for
SolidCraft `sketch.insert_svg` and an extrude (emboss 0.4-0.6 mm, deboss 0.4 mm).
"""
import math
import sys
from pathlib import Path

from shapely import affinity
from shapely.geometry import LineString, MultiPolygon, Point, Polygon
from shapely.ops import unary_union

OUT = Path(__file__).resolve().parent
Q = 16  # buffer segments per quarter circle

# --- dimensions (mm, badge Ø20) ---------------------------------------------
R_OUT, R_IN = 10.0, 8.6          # rotator ring (as Triton's orbit ring)
R_MID = (R_OUT + R_IN) / 2
GAP = 0.7                        # knockout between the beam and the ring
BEAM_W = 1.1
HEAD_HW, HEAD_H = 1.2, 1.9       # arrowhead half width, height (as Triton's tines)
BEAM_TIP = 11.4                  # = Triton's centre tine tip, OpenWheel's beam tip
SENSOR_W, SENSOR_H = 8.4, 5.6    # sensor frame outside, 3:2 (IMX571)
FRAME_W = 1.1                    # frame line
SENSOR_ANG = 20.0                # frame turned by the rotator (deg, CCW)
AXIS_R = 1.0                     # optical axis dot
ROT_HW, ROT_L = 1.2, 1.9         # ring arrowhead: radial half width, length along the ring
CLOSE = 0.28                     # notch rounding radius (fills gaps < 0.56 mm)


def sensor():
    hw, hh = SENSOR_W / 2, SENSOR_H / 2
    outer = Polygon([(-hw, -hh), (hw, -hh), (hw, hh), (-hw, hh)])
    inner = outer.buffer(-FRAME_W, join_style="mitre")
    frame = outer.difference(inner)
    g = unary_union([frame, Point(0, 0).buffer(AXIS_R, quad_segs=Q)])
    return affinity.rotate(g, SENSOR_ANG, origin=(0, 0))


def beam():
    base = BEAM_TIP - HEAD_H
    # the beam leaves the sensor frame where it crosses x = 0 (inside the frame line, so they join)
    start = SENSOR_H / 2 / math.cos(math.radians(SENSOR_ANG)) - FRAME_W / 2
    shaft = LineString([(0, start), (0, base + 0.1)]).buffer(BEAM_W / 2, quad_segs=Q, cap_style="flat")
    head = Polygon([(0, BEAM_TIP), (HEAD_HW, base), (BEAM_W / 2, base),
                    (-BEAM_W / 2, base), (-HEAD_HW, base)])
    return unary_union([shaft, head])


def ring():
    """The ring as a rotation arrow: open at the top for the beam, its right end an arrowhead
    pointing counter-clockwise towards the beam; the left end is a straight cut as in the siblings."""
    clear = HEAD_HW + GAP                                      # x of the cuts beside the beam
    tip_a = math.degrees(math.acos((clear) / R_MID))           # arrow tip angle (right side)
    base_a = tip_a - math.degrees(ROT_L / R_MID)
    ring = Point(0, 0).buffer(R_OUT, quad_segs=4 * Q).difference(Point(0, 0).buffer(R_IN, quad_segs=4 * Q))
    # remove the top sector from the arrow base (right) to the straight cut (left)
    left = Polygon([(-clear, 0), (0, 0), (0, 12), (-clear, 12)])
    wedge = Polygon([(0, 0)] + [(12 * math.cos(math.radians(a)), 12 * math.sin(math.radians(a)))
                                for a in [base_a + i * (90 - base_a) / 20 for i in range(21)]])
    ring = ring.difference(left).difference(wedge)
    b = math.radians(base_a)
    t = math.radians(tip_a)
    radial = (math.cos(b), math.sin(b))
    head = Polygon([((R_MID - ROT_HW) * radial[0], (R_MID - ROT_HW) * radial[1]),
                    ((R_MID + ROT_HW) * radial[0], (R_MID + ROT_HW) * radial[1]),
                    (R_MID * math.cos(t), R_MID * math.sin(t))])
    return unary_union([ring, head])


def badge():
    g = unary_union([ring(), sensor(), beam()])
    return g.buffer(CLOSE, quad_segs=Q).buffer(-CLOSE, quad_segs=Q).simplify(0.01)


def wordmark(text, cap_h, font):
    from matplotlib.font_manager import FontProperties
    from matplotlib.textpath import TextPath
    import numpy as np
    tp = TextPath((0, 0), text, size=1, prop=FontProperties(fname=font))
    polys, cur = [], []
    for bez, code in tp.iter_bezier():
        if code == tp.MOVETO:
            if len(cur) > 2:
                polys.append(Polygon(cur))
            cur = [tuple(bez.control_points[0])]
        elif code == tp.CLOSEPOLY:
            if len(cur) > 2:
                polys.append(Polygon(cur))
            cur = []
        else:
            n = 1 if bez.degree == 1 else 16
            cur += [tuple(p) for p in bez(np.linspace(0, 1, n + 1)[1:])]
    if len(cur) > 2:
        polys.append(Polygon(cur))
    geom = Polygon()  # even-odd: counters (O, P) become holes
    for p in sorted(polys, key=lambda p: -p.area):
        geom = geom.symmetric_difference(p)
    minx, miny, maxx, maxy = geom.bounds
    s = cap_h / (maxy - miny)
    return affinity.scale(geom, s, s, origin=(0, 0)), s


def lockup():
    b = badge()
    w, _ = wordmark("OPENROTO", 6.0, r"C:\Windows\Fonts\arialbd.ttf")
    minx, miny, _, maxy = w.bounds
    w = affinity.translate(w, R_OUT + 3.0 - minx, -(miny + maxy) / 2)
    return unary_union([b, w])


def polys(g):
    return list(g.geoms) if isinstance(g, MultiPolygon) else [g]


def to_svg(g, path, margin=0.5):
    minx, miny, maxx, maxy = g.bounds
    w, h = maxx - minx + 2 * margin, maxy - miny + 2 * margin

    def ring_d(coords):
        pts = [(x - minx + margin, maxy + margin - y) for x, y in coords]  # flip y
        return "M" + " L".join(f"{x:.3f},{y:.3f}" for x, y in pts[:-1]) + " Z"

    d = " ".join(ring_d(p.exterior.coords) + "".join(" " + ring_d(i.coords) for i in p.interiors)
                 for p in polys(g))
    path.write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.3f}mm" height="{h:.3f}mm" '
        f'viewBox="0 0 {w:.3f} {h:.3f}">\n'
        f'  <path fill="#000" fill-rule="evenodd" d="{d}"/>\n</svg>\n', encoding="utf-8")


def check(g, name):
    """FDM limits: thinnest line and narrowest gap, by erosion/dilation."""
    thin = g.difference(g.buffer(-0.45, quad_segs=Q).buffer(0.45, quad_segs=Q)).area
    gaps = g.buffer(0.3, quad_segs=Q).buffer(-0.3, quad_segs=Q).difference(g).area
    minx, miny, maxx, maxy = g.bounds
    print(f"{name}: {maxx - minx:.2f} x {maxy - miny:.2f} mm, {len(polys(g))} islands, "
          f"area {g.area:.1f} mm2, under-0.9 mm line area {thin:.3f}, under-0.6 mm gap area {gaps:.3f}")


def preview(items, path):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.patches import PathPatch
    from matplotlib.path import Path as MPath
    fig, axes = plt.subplots(1, len(items), figsize=(6 * len(items), 6),
                             gridspec_kw={"width_ratios": [g.bounds[2] - g.bounds[0] for g, _ in items]})
    for ax, (g, title) in zip(axes, items):
        ax.set_facecolor("#1c1c1f")  # black anodised aluminium
        for p in polys(g):
            verts, codes = [], []
            for r in [p.exterior, *p.interiors]:
                c = list(r.coords)
                verts += c
                codes += [MPath.MOVETO] + [MPath.LINETO] * (len(c) - 2) + [MPath.CLOSEPOLY]
            ax.add_patch(PathPatch(MPath(verts, codes), fc="#d0d0d6", ec="none"))
        minx, miny, maxx, maxy = g.bounds
        ax.set_xlim(minx - 1, maxx + 1); ax.set_ylim(miny - 1, maxy + 1)
        ax.set_aspect("equal"); ax.set_title(title); ax.tick_params(labelsize=7)
    fig.tight_layout(); fig.savefig(path, dpi=150); plt.close(fig)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    b, l = badge(), lockup()
    check(b, "badge"); check(l, "lockup")
    to_svg(b, OUT / "openroto_badge.svg")
    to_svg(l, OUT / "openroto_lockup.svg")
    preview([(b, "openroto_badge (mm)"), (l, "openroto_lockup (mm)")], OUT / "preview.png")
    print("written to", OUT)
