import json
from os import mkdir, remove, path
from typing import Union
import uuid

from source.py.utils import joinPaths
from source.py.task.merge_font.utils import instantiate, merge_fonts, polish

CONFIG_FILE = "config_merge.json"


def create_default_config():
    """Create a default config file (based on the example)."""
    default_config = {
        "family": "Test Font",
        "vertical_metric": {
            "ascender": 850,
            "descender": -250,
        },
        "output_dir": "./fonts",
        "config": [
            {
                "style": "Regular",
                "main": "/path/to/static/font.ttf",
                "other": {
                    "$PATH": "/path/to/variable/font.ttf",
                    "wght": 400,
                    "wdth": 100,
                },
            },
            {
                "style": "Bold",
                "main": {
                    "$PATH": "/path/to/variable/font.ttf",
                    "wght": 700,
                    "wdth": 110,
                },
                "other": "/path/to/static/font.ttf",
            },
        ],
    }

    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=2, ensure_ascii=False)
        print(f"Created default config file: {CONFIG_FILE}")
        print("Please edit the config file and re-run the script.")
    except Exception as e:
        print(f"Failed to create config file: {e}")

    exit(0)


def load_config() -> dict:
    """Load the config file."""
    if not path.exists(CONFIG_FILE):
        create_default_config()
        print("No config file, create and exit.")
        exit(1)

    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def resolve_font_source(
    source: Union[str, dict], output_dir: str, label: str
) -> tuple[str, bool]:
    """Resolve a font source entry.

    If `source` is a string, return it as-is.
    If `source` is a dict, instantiate a variable font and return a temporary path.

    Returns: (resolved_font_path, is_temporary_file)
    """
    if isinstance(source, str):
        if not path.exists(source):
            raise FileNotFoundError(f"Font file not found: {source}")
        return source, False

    if isinstance(source, dict):
        font_path = source.get("$PATH")
        if not font_path:
            raise ValueError(f"Configuration error: {label} missing $PATH field")

        if not path.exists(font_path):
            raise FileNotFoundError(f"Font file not found: {font_path}")

        # Extract axes value
        axes = {k: v for k, v in source.items() if k != "$PATH"}

        if not axes:
            # No axis params -> treat as a static font path
            return font_path, False

        print(f"Instantiating {label} from {font_path} with axes {axes}...")
        temp_filename = f"temp_{label}_{uuid.uuid4().hex[:8]}.ttf"
        temp_path = joinPaths(output_dir, temp_filename)

        instantiate(font_path, temp_path, axes)
        print(f"Instantiated temporary file: {temp_path}")
        return temp_path, True

    raise ValueError(f"Configuration error: {label} must be a string or an object")


def main():
    print("Font merge script (Experimental)")
    config_data = load_config()

    family_name = config_data.get("family", "Untitled")
    metric_data = config_data.get("vertical_metric", {})
    styles_config = config_data.get("config", [])
    output_dir = config_data.get("output_dir", "build")

    if not path.exists(output_dir):
        mkdir(output_dir)
        print(f"Created output directory: {output_dir}")

    line_metric = None
    if "ascender" in metric_data and "descender" in metric_data:
        line_metric = (
            int(metric_data["ascender"]),
            int(metric_data["descender"]),
        )

    # keep track of temporary files that need cleanup
    temp_files_to_clean = []
    # track final generated files to report at the end
    generated_files: list[str] = []

    for idx, item in enumerate(styles_config):
        style_name = item.get("style")
        main_source = item.get("main")
        other_source = item.get("other")

        print(f"\n{'=' * 60}")
        print(
            f"Processing [{idx + 1}/{len(styles_config)}]: {family_name} — {style_name}"
        )
        print(f"{'=' * 60}")

        # 1. Analyze Main Font
        try:
            current_main, is_main_temp = resolve_font_source(
                main_source, output_dir, f"{style_name}.main"
            )
        except Exception as e:
            print(f"Error resolving main font for {style_name}: {e}")
            print("Skipping this style.")
            continue

        if is_main_temp:
            temp_files_to_clean.append(current_main)

        if not path.exists(current_main):
            print(f"Main font does not exist: {current_main}. Skipping.")
            continue

        # 2. Analyze Other Font
        try:
            current_other, is_other_temp = resolve_font_source(
                other_source, output_dir, f"{style_name}.other"
            )
        except Exception as e:
            print(f"Error resolving other font for {style_name}: {e}")
            print("Skipping this style.")
            continue

        if is_other_temp:
            temp_files_to_clean.append(current_other)

        if not path.exists(current_other):
            print(f"Other font does not exist: {current_other}. Skipping.")
            continue

        # 3. Merge
        print("Merging fonts...")
        print(f" - main:  {current_main}")
        print(f" - other: {current_other}")
        merged_path = merge_fonts(output_dir, current_main, current_other)
        print(f"Merged temporary file: {merged_path}")

        temp_files_to_clean.append(merged_path)

        # 4. Polish
        print("Finalizing (naming and metrics)...")
        final_path = polish(
            font_path=merged_path,
            output_dir=output_dir,
            family_name=family_name,
            style_name=style_name,
            vertical_metric=line_metric,
        )
        print(f"Completed: {final_path}")
        if final_path and path.exists(final_path):
            generated_files.append(final_path)
        else:
            print(f"Final file not present after polish: {final_path}")

    # 5. Final cleanup
    print("\nCleaning up temporary files...")
    removed = 0
    failed = 0
    for temp_file in temp_files_to_clean:
        if path.exists(temp_file):
            try:
                remove(temp_file)
                removed += 1
            except Exception as e:
                print(f"Failed to remove {temp_file}: {e}")
                failed += 1

    print(f"Cleanup summary: removed={removed}, failed={failed}")
    print("\nAll tasks finished.")

    # Report generated files
    if generated_files:
        print("\nGenerated files:")
        for p in generated_files:
            print(f" - {p}")
    else:
        print("\nNo output files were generated.")
