# CAD video and animation views

Animations of the rotator are rendered straight from the SolidCraft assembly
(`cad/openroto_assembly.sc`), so they can be regenerated when the parts change. Nothing here is
saved into the assembly: the exploded views are created in the session and thrown away with it.

Output goes to `cad/_ref/video/` (ignored), except the README GIF, which is committed to `docs/`.

## Occurrence ids

From `component.list` on `cad/openroto_assembly.sc`:

| Part | Occurrence |
|---|---|
| Inner ring | 2 (grounded) |
| Spacer ring | 5 |
| Bearing RAU5005 | 8 |
| GT2 sleeve | 11 |
| Clamp ring | 14 |
| Outer ring | 59 |
| Pulley 12T | 35 |
| Belt 340 | 38 |
| Screws M2.5×8 | 41, 44, 47, 50, 53, 56 |

## `a_axial` — the axial explode

The whole rotator comes apart along the optical axis. The pulley and the belt are hidden: the 12T
pulley is still a typical envelope, not a measured part (see `cad/README.md`), so it is kept out of
anything published.

The order is the one in [`docs/label_exploded.py`](../../docs/label_exploded.py) — the published
exploded view — only spread wider so the parts separate on a phone screen. **Keep that order.** It
is the order the parts actually come apart in, and two pairs are easy to get backwards:

- The inner ring's **Ø52 flange sits above its Ø50 seat** (flange z 5.1…5.7, seat z −0.9…5.0), and
  the bearing bore is Ø50. So the bearing cannot pass the flange: it goes on from the **thread
  (camera) side** and leaves the same way. In the exploded view the inner ring is **above** the
  bearing, and the spacer below the bearing — the inner ring descends into them from the telescope
  side.
- The outer ring's **Ø77.9 belt flange is at the bottom** (z −1…0) with the Ø70 rim above it
  (z 0…4.8). The printed sleeve presses **down** onto that rim until it rests on the flange, and the
  clamp ring's spigot then enters the top of the sleeve bore. So the sleeve is **above** the outer
  ring.

```
browser.visibility {visible: true, isolate: true,
                    paths: [[2],[5],[8],[11],[14],[59],[41],[44],[47],[50],[53],[56]]}
explode.create {name: "a_axial", moves: [
    {occurrence: 41, translate: [0,0,130]},  // the six screws
    {occurrence: 44, translate: [0,0,130]},
    {occurrence: 47, translate: [0,0,130]},
    {occurrence: 50, translate: [0,0,130]},
    {occurrence: 53, translate: [0,0,130]},
    {occurrence: 56, translate: [0,0,130]},
    {occurrence: 14, translate: [0,0,109]},  // clamp ring
    {occurrence:  2, translate: [0,0,86]},   // inner ring
    {occurrence:  8, translate: [0,0,60]},   // bearing
    {occurrence:  5, translate: [0,0,47]},   // spacer ring
    {occurrence: 11, translate: [0,0,21]}]}  // GT2 sleeve (outer ring stays at 0)
```

Camera for every shot below (orthographic, `fov: 0`):

```
{target: [0,0,68], yaw: -0.7854, pitch: 0.32, distance: 285, fov: 0}
```

That projects at **8.5157 px/mm** with z 68 at y 958.7 in a 1080 × 1920 frame, solved from two
isolation renders (clamp ring and outer ring alone, differenced against the plate). The social
builder uses those numbers to place the part labels, so re-solve them if the camera changes.

### Reel frames (1080 × 1920)

```
motion.export_animation {view: "a_axial", back: false, samples: 61,
                         width: 1080, height: 1920, fps: 30, grid: false, axes: false,
                         camera: <above>, path: "<repo>/cad/_ref/video/a_explode"}
```

`back: false` exports the apart motion only; the hold and the reassembly are timed in the social
builder, which plays the frames forward, holds and plays them back.

### Background plate

The social builder cuts the parts out by differencing each frame against a plate — exact, and no
flood fill. The plate is the same camera with every occurrence hidden:

```
browser.visibility {visible: false, paths: [[2],[5],[8],[11],[14],[59],[41],[44],[47],[50],[53],[56],[35],[38]]}
screenshot {camera: <above>, width: 1080, height: 1920, grid: false, axes: false,
            path: "<repo>/cad/_ref/video/plate.png"}
```

Restore with the `browser.visibility` isolate call from the top.

### README GIF (`docs/openroto_explode.gif`)

```
motion.export_animation {view: "a_axial", back: true, samples: 61,
                         width: 460, height: 690, fps: 20, grid: false, axes: false,
                         camera: <above>, path: "<repo>/docs/openroto_explode.gif"}
```

`back: true` gives apart-and-together in one loop, which is what a README wants. Keep it small:
a GIF does not delta-compress, so every re-export adds its full size to the history for good. These
settings give about 0.9 MB; 640 × 960 at 81 frames gave 1.9 MB, which is too much for a figure.

## Where the Reel is built

`AstroInfra/social/tools/build_2026-11_openroto_explode.py` turns the frames into the 1080 × 1920
Reel (captions, part labels, end card, silent audio track). It reads the frames and the plate from
`cad/_ref/video/`, so export those first.
