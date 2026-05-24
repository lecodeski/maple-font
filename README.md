![Cover](./resources/header.png)

<p align="center">
  <a href="#Download">Download</a>
</p>

# Maple Mini

_Maple Mini_ is a fork of _Maple Mono_, the open-source monospace font focused on smoothing your coding flow.

[subframe7536](https://github.com/subframe7536) created _Maple Mono_ to enhance their working experience and hope that it can be useful to others.
Speaking for myself at least, I can say that his hope is fulfilled to some extent. Big thanks at this point!

V7 is a completely remade version, providing variable font format and source files of the font project, redesigning more than half of the glyphs and offering smarter ligatures. You can check out V6 [here](https://github.com/subframe7536/maple-font/tree/main)

## Fork

This repo, _Maple Mini_, is a fork of the original upstream repo redering my customizations and adjustments in the font to my favours. In particular, I reduced the line spacing to 0.83 (inspired by [CommitMono](https://commitmono.com/), another great coding font).  
This way this repo can be used also as an example, template, or simply inspiration on how to customize Maple Font, how to automize the update process and how to attach the build pipeline.  
Or go ahead and simply install my variant, _Maple Mini_, as documented below. Whatever floats your boat. =)

## Features

- ✨ Variable - Infinity font weights with fine-grained italic glyphs.
- ☁️ Smooth - Round corner, brand-new glyph of `@ $ % & Q ->` and cursive `f i j k l x y` in italic style.
- 💪 Useful - Large amount of smart ligatures, see in [`features/`](./source/features/README.md)
- 🎨 Icon - First-Class [Nerd-Font](https://github.com/ryanoasis/nerd-fonts) support, make your terminal more vivid.
- 🔨 Customize - Enable or disable font features as you want, just make your own font.

![2-1.png](./resources/2-1.png)

## ScreenShots

![showcase.png](./resources/showcase.png)

- Pictured by [CodeImg](https://github.com/subframe7536/vscode-codeimg)
- Theme: [Maple](https://github.com/subframe7536/vscode-theme-maple)
- Config: font size 16px, line height 1.8, default letter spacing

## Download

You can download all the font archives from [Releases](https://github.com/lecodeski/homebrew-maple-font/releases).

### Homebrew (MacOS, Linux)

```sh
# Maple Mini NF
brew install lecodeski/maple-font/font-maple-mini
```

<details>
  <summary>All packages (Click to expand)</summary>

  ```sh
  # Maple Mini
  brew install --cask font-maple-mini
  # Maple Mini NF
  brew install --cask font-maple-mini-nf
  # Maple Mini CN
  brew install --cask font-maple-mini-cn
  # Maple Mini NF CN
  brew install --cask font-maple-mini-nf-cn

  # Maple Mini Normal
  brew install --cask font-maple-mini-normal
  # Maple Mini Normal NF
  brew install --cask font-maple-mini-normal-nf
  # Maple Mini Normal CN
  brew install --cask font-maple-mini-normal-cn
  # Maple Mini Normal NF CN
  brew install --cask font-maple-mini-normal-nf-cn
  ```

</details>

## Usage & Feature Configurations

See in [document](./source/features/README.md) or try it in [Playground](https://font.subf.dev/en/playground)

## Naming FAQ

### Features

- **Ligature**: Default version with ligatures (`Maple Mini`)
- **No-Ligature**: Default version without ligatures (`Maple Mini NL`)
- **Normal-Ligature**: [`--normal` preset](#preset) with ligatures (`Maple Mini Normal`)
- **Normal-No-Ligature**: [`--normal` preset](#preset) without ligatures (`Maple Mini Normal NL`)

### Format and Glyph Set

- **Variable**: Minimal version, smoothly change font weight by variable
- **TTF**: Minimal version, ttf format [Recommend!]
- **OTF**: Minimal version, otf format
- **WOFF2**: Minimal version, woff2 format, for small size on web pages
- **NF**: Nerd-Font patched version, add icons for terminal (With `-NF` suffix)
- **CN**: Chinese version, embed with Chinese and Japanese glyphs (With `-CN` suffix)
- **NF-CN**: Full version, embed with icons, Chinese and Japanese glyphs (With `-NF-CN` suffix)

### Font Hint

- **Hinted font** is used for low resolution screen to have better render effect. From my experience, if your screen resolution is lower or equal than 1080P, it is recommended to use "hinted font". Using "unhinted font" will lead to misalignment or uneven thickness on your text.
  - In this case, you can choose `MapleMini-TTF-AutoHint` / `MapleMini-NF` / `MapleMini-NF-CN`, etc.
- **Unhinted font** is used for high resolution screen (e.g. for MacBook). Using "hinted font" will blur your text or make it looks weird.
  - In this case, you can choose `MapleMini-OTF` / `MapleMini-TTF` / `MapleMini-NF-unhinted` / `MapleMini-NF-CN-unhinted`, etc.
- Why there exists `-AutoHint` and `-unhinted` suffix?
  - for backward compatibility, I keep the original naming scheme. `-AutoHint` is only used for `TTF` format.

## Custom Build

The [`config.json`](./config.json) file is used to configure the build process. Checkout the [schema](./source/schema.json) or [document](./source/features/README.md) for more details.

There also have some [command line options](#build-script-usage) for customizing the build process. Cli options have higher priority than options in `config.json`.

### Build Methods

#### 1. Build In Browser

Go to [Playground](https://font.subf.dev/en/playground), and click "Custom Build" button in the bottom left corner

- Only support freezing OpenType features currently.

#### 2. Use Github Actions

You can use [Github Actions](https://github.com/lecodeski/homebrew-maple-font/actions/workflows/custom.yml) to build the font.

1. Fork the repo
2. (Optional) Change the content in `config.json`
3. Go to Actions tab
4. Click on `Custom Build` menu item on the left
5. Click on `Run workflow` button with options setup
6. Wait for the build to finish
7. Download the font archives from Releases

#### 3. Use Docker

```shell
git clone https://github.com/lecodeski/homebrew-maple-font --depth 1 -b variable
docker build -t maple-font .
docker run -v "$(pwd)/fonts:/app/fonts" -e BUILD_ARGS="--normal" maple-font
```

#### 4. Local Build

Clone the repo and run on your local machine. Make sure you have `python3` and `pip` installed

```shell
git clone https://github.com/lecodeski/homebrew-maple-font --depth 1 -b variable
pip install -r requirements.txt
python build.py
```

> [!TIP]
> For `Ubuntu` or `Debian`, maybe `python-is-python3` is needed as well.
>
> If you have trouble installing the dependencies, just create a new GitHub Codespace and run the commands there.

### Narrow Glyph Width

You can setup `"width": "narrow"` in `config.json` or add `--width slim` in cli flag to change glyph width at build time.

There are 3 options:
- default: 600
- narrow: 550
- slim: 500

Preview: [#131](https://github.com/subframe7536/maple-font/issues/131#issuecomment-3678666194)

### Custom Nerd-Font

If you want to get fixed width icons, setup `"nerd_font.mono": true` in `config.json` or add `--nf-mono` flag to build script args.

If you want to get variable width icons, setup `"nerd_font.propo": true` in `config.json` or add `--nf-propo` flag to build script args.

For custom `font-patcher` args, `font-forge` (and maybe `python3-fontforge` as well) is required.

Maybe you should also change `"nerd_font.extra_args"` in [config.json](./config.json)

Default args: `-l --careful --outputdir dir`
- if `"nerd_font.propo"` is `true`, then add `--variable-width-glyphs`
- else if `"nerd_font.mono"` is `true`, then add `--mono`

### Preset

Run `build.py` with `--normal` flag, make the font looks not such "Opinioned" , just like `JetBrains Mono` (with slashed zero).

If you are using variable font (NOT recommended), please enable `calt` to make all features work.

Enabled features:
<!-- NORMAL -->
```
cv01, cv02, cv33, cv34, cv35, cv36, cv61, cv62, ss05, ss06, ss07, ss08
```
<!-- NORMAL -->

[Online Preview](https://font.subf.dev/en/playground?normal)

### Freeze OpenType Feature

There are three kinds of options for feature freeze ([Why](https://github.com/subframe7536/maple-font/issues/233#issuecomment-2410170270)):

1. `enable`: Forcely enable the features without setting up `cvXX` / `ssXX` / `zero` in font features config, just as default glyphs / ligatures
2. `disable`: Remove the features in `cvXX` / `ssXX` / `zero`, which will no longer effect, even if you enable it manually
3. `ignore`: Do nothing

#### Custom OpenType Feature

OpenType Feature is used to control the font's built-in variants and ligatures. You can remove some ligatures or features you don't want to, change feature's trigger rule or add some new rules by modifying OpenType Feature.

By default, the Python module in [`source/py/feature/`](./source/py/feature) will generate feature rule string and load it at build time. You can modify the features or customize tags there.

If you would like to modify the feature file instead, run `build.py` with `--apply-fea-file` flag, the feature file from [`source/features/{regular,italic}{_cn,}.fea`](./source/features) will be loaded.

### Infinite Arrow Ligatures

Inspired by Fira Code, the font enables infinite arrow ligatures by default from v7.3. For some reason, the ligatures are misaligned when using hinted font, so they are removed in hinted version by default from v7.4.

You can setup `"infinite_arrow": true` in `config.json` or add `--infinite-arrow` in cli flag to force enabling the feature. See more details in [#508](https://github.com/subframe7536/maple-font/issues/508)

### Custom Font Weight Mapping

You can modify the static font weight through `"weight_mapping"` item in `config.json`.

For example, if you want to make regular font weight a little bit lighter, just decrease the number of `"weight_mapping.regular"` (from 400 to 350 in this example) :

```json
{
  "weight_mapping": {
    "thin": 100,
    "extralight": 200,
    "light": 300,
    "regular": 350,
    "semibold": 500,
    "medium": 600,
    "bold": 700,
    "extrabold": 800
  }
}
```

#### GitHub Mirror

The build script will auto download required assets from GitHub. If you have trouble downloading, please setup `github_mirror` in [config.json](./config.json) or `$GITHUB` to your environment variable. (Target URL will be `https://<github_mirror>/<user>/<repo>/releases/download/<tag>/<file>`), or just download the target `.zip` file and put it in the same directory as `build.py`.

#### Traditional Chinese Punctuation Support

By enabling `cv99`, all Chinese punctuation marks will be centred. See more details in [#150](https://github.com/subframe7536/maple-font/issues/150)

### Build Script Usage

```
usage: build.py [-h] [-v] [-d] [--debug] [-n] [--feat FEAT] [--apply-fea-file]
                [--hinted | --no-hinted] [--liga | --no-liga] [--keep-infinite-arrow]
                [--infinite-arrow] [--remove-tag-liga] [--line-height LINE_HEIGHT]
                [--width {default,narrow,slim}] [--nf-mono] [--nf-propo]
                [--nf | --no-nf]
                [--ttf-only] [--least-styles]
                [--font-patcher] [--cache] [--archive]

✨ Builder and optimizer for Maple Mini

options:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d, --dry             Output config and exit
  --debug               Add `Debug` suffix to family name and faster build

Feature Options:
  -n, --normal          Use normal preset, just like `JetBrains Mono` with slashed
                        zero
  --feat FEAT           Freeze font features, splited by `,` (e.g. `--feat
                        zero,cv01,ss07,ss08`). No effect on variable format
  --apply-fea-file      Load feature file from `source/features/{regular,italic}.fea`
                        to variable font
  --hinted              Use hinted font as base font in NF (default)
  --no-hinted           Use unhinted font as base font in NF
  --liga                Preserve all the ligatures (default)
  --no-liga             Remove all the ligatures
  --infinite-arrow      Enable infinite arrow ligatures (Disabled in hinted font by
                        default)
  --remove-tag-liga     Remove plain text tag ligatures like `[TODO]`
  --line-height LINE_HEIGHT
                        Scale factor for line height (e.g. 1.1)
  --width {default,narrow,slim}
                        Set glyph width: default (600), narrow (550), slim (500)
  --nf-mono             Make Nerd Font icons' width fixed
  --nf-propo            Make Nerd Font icons' width variable, override `--nf-mono`

Build Options:
  --nf, --nerd-font     Build Nerd-Font version (default)
  --no-nf, --no-nerd-font
                        Do not build Nerd-Font version
  --ttf-only            Only build TTF format
  --least-styles        Only build Regular / Bold / Italic / BoldItalic style
  --font-patcher        Force the use of Nerd Font Patcher to build NF format
  --cache               Reuse font cache of TTF, OTF and Woff2 formats
  --archive             Build font archives with config and license. If has `--cache`
                        flag, only archive NF and CN formats
```

## Development

### Design

Using [FontLab](https://www.fontlab.com/) or [Glyphs](https://glyphs.app), generate variable TTF into `source/` folder.

### Build

```sh
# Init project
uv sync
# Dev
uv run build.py --ttf-only --debug
# Update nerd font
uv run task.py nerd-font
# Update fea file
uv run task.py fea
# Update landing page info
uv run task.py page --sync
# Merge two fonts
uv run task.py merge
# Release
uv run task.py release minor
```

## Credit

- [subframe7536](https://github.com/subframe7536)
- [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono)
- [Roboto Mono](https://github.com/googlefonts/RobotoMono)
- [Fira Code](https://github.com/tonsky/FiraCode)
- [Victor Mono](https://github.com/rubjo/victor-mono)
- [Commit Mono](https://github.com/eigilnikolajsen/commit-mono)
- [Code Sample](https://github.com/TheRenegadeCoder/sample-programs-website)
- [Nerd Font](https://github.com/ryanoasis/nerd-fonts)
- [Font Freeze](https://github.com/MuTsunTsai/fontfreeze/)
- [Font Viewer](https://tophix.com/font-tools/font-viewer)
- [Monolisa](https://www.monolisa.dev/)
- [Recursive](https://www.recursive.design/)

## License

SIL Open Font License 1.1
