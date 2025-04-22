# Ligatures And Features

Here is the check list and explaination of Maple Mono ligatures and features.

For more details, please check out `.fea` files in same directory and [OpenType Feature Spec](https://adobe-type-tools.github.io/afdko/OpenTypeFeatureFileSpecification.html).

## Usage

### VSCode

Setup in your VSCode settings json file

```jsonc
{
  // Setup font family
  "editor.fontFamily": "Maple Mono NF, Jetbrains Mono, Menlo, Consolas, monospace",
  // Enable ligatures
  "editor.fontLigatures": "'calt'",
  // Or enable OpenType features
  "editor.fontLigatures": "'calt', 'cv01', 'ss01', 'zero'",
}
```

### IDEA / Pycharm / WebStorm / GoLand / CLion

1. Open Settings
2. Click "Editor"
3. Click "Font"
4. Choose "Maple Mono NF" in the font menu
5. Click "Enable Ligatures"

OpenType Features are not supported, you need to custom build to freeze features.

## Ligatures

"Enable ligature", is same as "enable `calt` feature":

<!-- CALT -->
```
::
:::
?:
:?
:?>
:=
=:
:=:
=:=
<:
:>
:<
<:<
>:>
::=
__
#{
#[
#(
#?
#!
#:
#=
#_
#__
#_(
]#
#######
<<
<<<
>>
>>>
{{
}}
{|
|}
{{--
{{!--
--}}
[|
|]
!!
||
??
???
&&
&&&
//
///
/*
/**
*/
++
+++
--
---
;;
;;;
..
...
.?
?.
..<
.=
<~
~>
~~
<~>
<~~
~~>
-~
~-
~@
0xA12 0x56 1920x1080
<=>
<==>
>=
<=
<==
==>
=>
<=<
>=>
<=|
|=>
==
===
!=
!==
=/=
=!=
=<=
=>=
|=
||=
\\ \' \.
<!--
<#--
<!---->
<->
->
<-
-->
<--
<-<
>->
<-|
|->
<|||
|||>
<||
||>
<|
|>
<|>
-|
|-
_|_
||-
<>
</
/>
</>
<+
+>
<+>
<*
*>
<*>
[TRACE]
[DEBUG]
[INFO]
[WARN]
[ERROR]
[FATAL]
[TODO]
[FIXME]
[NOTE]
[HACK]
[MARK]
[EROR]
[WARNING]
todo))
fixme))
```
<!-- CALT -->

### Notice

- `>>` / `>>>` is smart, but much contextual-sensitive, so it may be not effect in some IDEs ([explaination](https://github.com/subframe7536/maple-font/discussions/275)). Turn on `ss07` to force enable.

## Features

### Character Varients (cvXX)

<!-- CV -->
- [7.0] cv01: Normalize special symbols (`@ $ & % Q => ->`)
- [7.0] cv02: Alternative `a` with top arm, no effect in italic style
- [7.0] cv03: Alternative `i` without left bottom bar
- [7.0] cv04: Alternative `l` with left bottom bar, like consolas, will be overrided by `cv35` in italic style
- [7.1] cv05: Alternative `g` in double story style, no effect in italic style
- [7.1] cv06: Alternative `i` without bottom bar, no effect in italic style
- [7.1] cv07: Alternative `J` without top bar, no effect in italic style
- [7.1] cv08: Alternative `r` with bottom bar, no effect in italic style
- [7.1] cv61: Alternative `,` and `;` with straight tail
- [7.1] cv62: Alternative `?` with larger openings
- [7.1] cv63: Alternative `<=` in arrow style
- [7.0] zero: Dot style `0`
<!-- CV -->

#### Italic Only

<!-- CV-IT -->
- [7.0] cv31: Alternative italic `a` with top arm
- [7.0] cv32: Alternative Italic `f` without bottom tail
- [7.0] cv33: Alternative Italic `i` and `j` with left bottom bar and horizen top bar
- [7.0] cv34: Alternative Italic `k` without center circle
- [7.0] cv35: Alternative Italic `l` without center tail
- [7.0] cv36: Alternative Italic `x` without top and bottom tails
- [7.0] cv37: Alternative Italic `y` with straight intersection
- [7.1] cv38: Alternative italic `g` in double story style
- [7.1] cv39: Alternative Italic `i` without bottom bar
- [7.1] cv40: Alternative italic `J` without top bar
- [7.1] cv41: Alternative italic `r` with bottom bar
<!-- CV-IT -->

#### CN Only

<!-- CV-CN -->
- [7.0] cv96: Full width quotes (`“` / `”` / `‘` / `’`)
- [7.0] cv97: Full width ellipsis (`…`)
- [7.0] cv98: Full width emdash (`—`)
- [7.0] cv99: Traditional centered punctuations
<!-- CV-CN -->

### Stylistic Sets (ssXX)

<!-- SS -->
- [7.0] ss01: Broken multiple equals ligatures (`==`, `===`, `!=`, `!==` ...)
- [7.0] ss02: Broken compare and equal ligatures (`<=`, `>=`)
- [7.0] ss03: Allow to use any case in all tags
- [7.0] ss04: Broken multiple underscores ligatures (`__`, `#__`)
- [7.0] ss05: Revert thin backslash in escape symbols (`\\`, `\"`, `\.` ...)
- [7.0] ss06: Break connected strokes between italic letters (`al`, `il`, `ull` ...)
- [7.0] ss07: Relax the conditions for multiple greaters ligatures (`>>` or `>>>`)
- [7.0] ss08: Double headed arrows and reverse arrows ligatures (`>>=`, `-<<`, `->>`, `>-` ...)
- [7.1] ss09: Asciitilde equal as not equal to ligature (`~=`)
- [7.1] ss10: Approximately equal to and approximately not equal to ligatures (`=~`, `!~`)
- [7.1] ss11: Equal and extra punctuation ligatures (`|=`, `/=`, `?=`, `&=`, ...)
<!-- SS -->