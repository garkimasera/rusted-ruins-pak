#!/bin/bash
shopt -s globstar
makepak=rusted-ruins-makepak
srcdir=paksrc
destdir=paks

mkdir -p $destdir
$makepak $srcdir/anim/**/*.toml           -o $destdir/anim.pak
$makepak $srcdir/chara_template/**/*.toml -o $destdir/chara_template.pak
$makepak $srcdir/deco/**/*.toml           -o $destdir/deco.pak
$makepak $srcdir/effect/**/*.toml         -o $destdir/effect.pak
$makepak $srcdir/item/**/*.toml           -o $destdir/item.pak
$makepak $srcdir/special_tile/**/*.toml   -o $destdir/special_tile.pak
$makepak $srcdir/tile/**/*.toml           -o $destdir/tile.pak
$makepak $srcdir/ui_img/**/*.toml         -o $destdir/ui_img.pak
$makepak $srcdir/wall/**/*.toml           -o $destdir/wall.pak
$makepak $srcdir/region_gen/**/*.toml     -o $destdir/region_gen.pak
$makepak $srcdir/site_gen/**/*.toml       -o $destdir/site_gen.pak
$makepak $srcdir/talk_script/**/*.toml    -o $destdir/talk_script.pak
