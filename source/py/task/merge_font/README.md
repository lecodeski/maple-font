## merge_font

Short utilities for merging and polishing TrueType/OpenType fonts used by the build tasks.

> [!note]
I use it to create my daily sans font [Maple Sans](https://github.com/subframe7536/maple-font/releases/tag/cn-base) —— SF Pro Rounded + 汉仪正圆

### Requirements

- Python packages: `foundrytools`.
- FontForge (for running `merger.py` or when the utilities shell out to the `fontforge` binary).

### Usage

1. Using the small FontForge script directly under FontForge's Python environment, or with `fontforge -script` depending on your setup

```sh
/path/to/ffpython source/py/task/merge_font/merger.py path/to/fontA.ttf path/to/fontB.ttf path/to/output.ttf
```

```sh
fontforge -script source/py/task/merge_font/merger.py path/to/fontA.ttf path/to/fontB.ttf path/to/output.ttf
```

2. From Python build tasks

```sh
uv run task.py merge
```

If config file not exists, it will be auto created. Example:

```json
{
  "family": "My Font",
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
```