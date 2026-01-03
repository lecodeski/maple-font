from os import makedirs, system, path
from shutil import rmtree
from uuid import uuid4
from fontTools.ttLib import TTFont
from fontTools.ttLib.tables._f_v_a_r import NamedInstance
from fontTools.subset import Subsetter

from source.py.utils import (
    adjust_line_height,
    get_font_forge_bin,
    joinPaths,
    parse_style_name,
    run,
    set_font_name,
    update_font_names,
)
from foundrytools import Font
from foundrytools.app.var2static import run as var2static


def subset(main_font_path: str, other_font_path: str, output_path: str):
    other_font = TTFont(other_font_path)
    removeUnicodes = set()
    for t in other_font["cmap"].tables:  # type: ignore
        if t.isUnicode():
            removeUnicodes.update(t.cmap.keys())
    other_font.close()

    font = TTFont(main_font_path)
    target_unicode = set()
    for t in font["cmap"].tables:  # type: ignore
        if t.isUnicode():
            target_unicode = set(t.cmap.keys()).difference(removeUnicodes)

    subsetter = Subsetter()
    subsetter.populate(
        unicodes=target_unicode,
    )
    subsetter.subset(font)
    font.save(output_path)


def merge_fonts(
    output_dir: str,
    main_font_path: str,
    other_font_path: str,
) -> str:
    """
    Merge two fonts into one.

    :param output_dir: The output directory to save the merged font.
    :param main_font_path: The path to the main font file.
    :param other_font_path: The path to the other font file to merge.
    :return: The path to the merged font file.
    """
    tmp_dir = joinPaths(
        output_dir,
        "tmp",
    )
    makedirs(tmp_dir, exist_ok=True)
    subset_path = joinPaths(tmp_dir, f"tmp_subset_{uuid4().hex[:8]}.ttf")
    subset(
        main_font_path,
        other_font_path,
        subset_path,
    )
    bin = get_font_forge_bin()
    if bin is None:
        print("No fontforge bin detected, try to use the `fontforge` command directly")
        bin = "fontforge"

    target_path = joinPaths(output_dir, path.basename(subset_path))
    run(
        [
            bin,
            "source/py/task/merge_font/merger.py",
            subset_path,
            other_font_path,
            target_path,
        ]
    )
    rmtree(tmp_dir, ignore_errors=True)
    return target_path


def instantiate(input_font_path: str, output_font_path: str, config: dict) -> None:
    """
    Instantiate a variable font with the given configuration.

    :param input_font_path: The path to the input font file.
    :param output_font_path: The path to the output font file.
    :param config: A dictionary containing axis configurations.
    """
    f = Font(input_font_path)
    coordinates = {}
    instance = NamedInstance()
    for a in f.t_fvar.table.axes:
        axis_tag = a.axisTag
        min_value = a.minValue
        max_value = a.maxValue
        val = config.get(axis_tag, a.defaultValue)
        if min_value > val or max_value < val:
            raise Exception(f"Invalid axe value, range: [{min_value}, {max_value}]")
        coordinates[axis_tag] = val

    instance.coordinates = coordinates

    static_font, file_base_name = var2static(f, instance)
    static_font.save(output_font_path)
    static_font.close()
    f.close()


def _get_glyph_bounds(font, glyph_name):
    """Get (yMin, yMax) of a glyph by name from 'glyf' table."""
    glyph_order = font.getGlyphOrder()
    if glyph_name not in glyph_order:
        raise ValueError(f"Glyph '{glyph_name}' not found in font.")
    glyf = font["glyf"]
    glyph = glyf[glyph_name]
    if glyph.numberOfContours == 0:
        # Empty glyph
        return (0, 0)
    y_min = glyph.yMin
    y_max = glyph.yMax
    return (y_min, y_max)


def auto_xheight_capheight(font: TTFont):
    if "OS/2" not in font:
        raise ValueError("Font does not have an OS/2 table.")
    if "glyf" not in font:
        raise ValueError(
            "This script only supports TrueType (glyf) fonts. CFF support not implemented."
        )

    # Get bounds
    z_ymin, z_ymax = _get_glyph_bounds(font, "z")
    Z_ymin, Z_ymax = _get_glyph_bounds(font, "Z")

    x_height = round(z_ymax)  # xHeight = top of lowercase 'z'
    cap_height = round(Z_ymax)  # capHeight = top of uppercase 'Z'

    # Update OS/2 table
    os2 = font["OS/2"]
    os2.sxHeight = x_height  # type: ignore
    os2.sCapHeight = cap_height  # type: ignore


def polish(
    font_path: str,
    output_dir: str,
    family_name: str,
    style_name: str,
    vertical_metric: tuple[float, float] | None,
) -> str:
    """
    Clean up the font by adjusting line height and updating font names.

    :param font_path: The path to the font file.
    :param output_dir: The output directory to save the cleaned font.
    :param family_name: The family name of the font.
    :param style_name: The style name of the font.
    :param vertical_metric: A tuple containing vertical metric values, or None.
    """
    font = TTFont(font_path)
    if vertical_metric:
        adjust_line_height(font, 1, vertical_metric)

    auto_xheight_capheight(font)

    postscript_name = f"{family_name.replace(' ', '')}-{style_name}"
    style_with_prefix_space, style_in_2, style_in_17, is_skip_subfamily, is_italic = (
        parse_style_name(
            style_name_compact=style_name,
        )
    )
    version = "1.000"
    update_font_names(
        font=font,
        family_name=family_name + style_with_prefix_space,
        style_name=style_in_2,
        full_name=f"{family_name} {style_in_17}",
        version_str=version,
        postscript_name=postscript_name,
        unique_identifier=f"{version};SUBF;{postscript_name};",
        is_skip_subfamily=is_skip_subfamily,
        preferred_family_name=family_name,
        preferred_style_name=style_in_17,
    )

    set_font_name(font, "", 0)
    prod_path = joinPaths(output_dir, f"{postscript_name}.ttf")
    font.save(prod_path)

    system(f"ftcli name del-mac-names {prod_path}")
    return prod_path
