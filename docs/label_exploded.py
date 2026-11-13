"""Crop the SolidCraft exploded render and add numbered callouts matching docs/BOM.md.

Render: a SolidCraft design linking every cad/*.sc part (component.insert_design) with Z offsets
outer ring 0, sleeve +16 (belt +16.25, pulley at (0, 97.9, +8.75)), spacer +36, bearing +46,
inner ring +66, clamp +84, screws with their head top at z 108.3 on the Ø65 circle (60° apart);
appearances: the four Al rings #1c1c1f (metallic 0.6, roughness 0.6), sleeve #2f6db5 (roughness 0.45),
belt #141414 (roughness 0.8), dielectric_ior 1.5;
camera {target: [0, 35, 46], yaw: 2.3, pitch: 0.32, distance: 300}, 1400 x 1200, no grid or axes.
Usage: python -I docs/label_exploded.py <render.png> docs/openroto_exploded.png
"""
import sys
from PIL import Image, ImageDraw, ImageFont

src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("RGB")
# crop: (left, top, right, bottom) in render pixels
box = (360, 190, 1080, 900)
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
    ("6", "6× screw DIN 7991 M2.5×8", (989, 280), 60),
    ("3", "Clamp ring (milled Al)", (1024, 345), 135),
    ("1", "Inner ring (milled Al)", (962, 460), 210),
    ("5", "Bearing THK RAU5005", (982, 550), 285),
    ("2", "Spacer ring (milled Al)", (966, 615), 360),
    ("4b", "GT2 sleeve (printed PETG)", (1021, 690), 435),
    ("4a", "Outer ring (milled Al)", (1023, 785), 510),
    ("8", "GT2 belt 340 mm", (760, 757), 585),
    ("7", "GT2 pulley 12T (on motor)", (455, 830), 660),
]
lx = im.width + 40
for n, text, (px, py), ly in items:
    ax, ay = px - ox, py - oy
    d.line([(ax, ay), (lx - 22, ly)], fill=(60, 60, 70), width=2)
    d.ellipse([ax - 4, ay - 4, ax + 4, ay + 4], fill=(200, 60, 40))
    r = 19
    d.ellipse([lx - r - 6, ly - r, lx + r - 6, ly + r], fill=(200, 60, 40))
    d.text((lx - 6, ly), str(n), font=f_num, fill="white", anchor="mm")
    d.text((lx + 20, ly), text, font=f_txt, fill=(30, 30, 35), anchor="lm")
d.text((20, 14), "Telescope side up. Motor (9) not shown.", font=font(18), fill=(70, 70, 80))
canvas.save(dst, optimize=True)
print(canvas.size)
