# docs

- [`PARTS.md`](PARTS.md) — what each part is, its material and how to make it.
- [`BOM.md`](BOM.md) — bill of materials for one OpenRoto.
- [`ASSEMBLY.md`](ASSEMBLY.md) — tools, assembly steps, belt tension and the final check.
- [`openroto_exploded.png`](openroto_exploded.png) — exploded view, numbered as the BOM;
  [`label_exploded.py`](label_exploded.py) adds the callouts to the SolidCraft render (how the render
  is made is in its docstring).
- [`section_clamp_contact.png`](section_clamp_contact.png) — half section at the clamp ring, made by
  [`make_section.py`](make_section.py) from the drawing profiles.
- [`cnc/`](cnc/) — JLCCNC order package for the milled rings: order guide, PDF drawings and the
  script that makes them.
