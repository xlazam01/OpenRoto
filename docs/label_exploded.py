"""Crop the SolidCraft exploded render and add numbered callouts matching docs/BOM.md.

Render: a SolidCraft design linking every cad/*.sc part (component.insert_design) with Z offsets
sleeve 0, spacer +22, bearing +32, inner ring +52, clamp +70, screws +86 (above their seat),
camera {target: [0, 35, 40], yaw: 2.3, pitch: 0.32, distance: 300}, 1400 x 1200, no grid or axes.
Usage: python -I docs/label_exploded.py <render.png> docs/openroto_exploded.png
"""
import sys
from PIL import Image, ImageDraw, ImageFont

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
# crop: (left, top, right, bottom) in render pixels
box = (360, 220, 1080, 930)
im = im.crop(box)
ox, oy = box[0], box[1]
pad_r = 430
canvas = Image.new("RGB", (im.width + pad_r, im.height), im.getpixel((im.width - 1, 5)))
# extend background gradient by copying the right-most column
col = im.crop((im.width - 1, 0, im.width, im.height))
for x in range(im.width, canvas.width):
    canvas.paste(col, (x, 0))
canvas.paste(im, (0, 0))
d = ImageDraw.Draw(canvas)

def font(sz, bold=False):
    for name in (("segoeuib.ttf" if bold else "segoeui.ttf"), "arial.ttf"):
        try:
            return ImageFont.truetype(name, sz)
        except OSError:
            pass
    return ImageFont.load_default()

f_num, f_txt = font(22, True), font(21)
# (number, label, anchor point on the part in render px, label y)
items = [
    (6, "6× screw DIN 7991 M2.5×8", (990, 300), 70),
    (3, "Clamp ring (milled Al)", (1022, 380), 165),
    (1, "Inner ring (milled Al)", (958, 490), 270),
    (5, "Bearing THK RAU5005", (982, 590), 370),
    (2, "Spacer ring (milled Al)", (966, 655), 450),
    (4, "Outer ring + GT2 sleeve (drawn as one)", (1022, 735), 530),
    (8, "GT2 belt 340 mm", (760, 820), 620),
    (7, "GT2 pulley 12T (on motor)", (455, 880), 690),
]
lx = im.width + 40
for n, text, (px, py), ly in items:
    ax, ay = px - ox, py - oy
    d.line([(ax, ay), (lx - 22, ly)], fill=(60, 60, 70), width=2)
    d.ellipse([ax - 4, ay - 4, ax + 4, ay + 4], fill=(200, 60, 40))
    r = 16
    d.ellipse([lx - r - 6, ly - r, lx + r - 6, ly + r], fill=(200, 60, 40))
    d.text((lx - 6, ly), str(n), font=f_num, fill="white", anchor="mm")
    d.text((lx + 20, ly), text, font=f_txt, fill=(30, 30, 35), anchor="lm")
d.text((20, 14), "Telescope side up. Motor (9) not shown.", font=font(18), fill=(70, 70, 80))
canvas.save(dst, optimize=True)
print(canvas.size)
