#!/usr/bin/env python
import sys

try:
    import fontforge  # type: ignore
except ImportError:
    print(
        "Cannot import fontforge module. Please ensure FontForge is installed and use its Python environment to run this script."
    )
    sys.exit(1)


def merge_fonts(font1_path, font2_path, output_path):
    font1 = fontforge.open(font1_path)
    upem1 = font1.em

    font2 = fontforge.open(font2_path)
    upem2 = font2.em

    if upem1 != upem2:
        scale = upem1 / upem2
        font2.transform((scale, 0, 0, scale, 0, 0))
        font2.em = upem1

    # for g in font2.glyphs():
    #     g.width = int(g.width * 1.065)

    font1.mergeFonts(font2)

    font1.generate(output_path)
    font1.close()
    font2.close()
    print(f"Merged font saved to: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(
            "Usage: /path/to/fontforge merge.py <font1_path> <font2_path> <output_path>"
        )
        sys.exit(1)

    path1 = sys.argv[1]
    path2 = sys.argv[2]
    out_path = sys.argv[3]
    merge_fonts(path1, path2, out_path)
