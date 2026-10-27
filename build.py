"""Build assets/*-{dark,light}.svg from assets/src/*.svg.

To change a number: edit the source SVG (text and aria-label), the matching
caption/alt text and table row in README.md, then run `python3 build.py`.
Fonts are base64 subsets in assets/src/{fonts,serif}.css; re-make them only for new glyphs.
"""
import pathlib, re, sys

PALETTES = {
    "dark": dict(card="#151a20", rule="#252c34", ink="#d6dbe0", mut="#868f99", acc="#9cc9bb", bad="#dc9a91",
                 h1="#7fb8a8", h2="#93bfa0", h3="#b8c59a"),
    "light": dict(card="#ffffff", rule="#d9ddd7", ink="#1f2429", mut="#5f6870", acc="#2f7d6d", bad="#b0473c",
                  h1="#2f7d6d", h2="#4a7f55", h3="#5f6b2f"),
}
src = pathlib.Path(__file__).parent / "assets" / "src"
fonts, serif = (src / "fonts.css").read_text(), (src / "serif.css").read_text()
ok = True
for svg in sorted(src.glob("*.svg")):
    text = svg.read_text().replace("/*FONTS*/", fonts).replace("/*SERIF*/", serif)
    for name, pal in PALETTES.items():
        out = re.sub(r"var\(--(\w+)\)", lambda m: pal[m.group(1)], text)
        path = src.parent / f"{svg.stem}-{name}.svg"
        path.write_text(out)
        kb = len(out.encode()) / 1024
        print(f"{path.name:28} {kb:5.1f} KB")
        ok &= kb <= 80
sys.exit(0 if ok else "an output is over 80 KB")
