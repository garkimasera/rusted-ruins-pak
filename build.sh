#!/bin/bash
shopt -s globstar

srcdir=paksrc
destdir=paks

if [ -n "$1" ]; then
    makepak=$1
else
    makepak=rusted-ruins-makepak
fi

mkdir -p $destdir
$makepak $srcdir/anim/**/*.ron           -o $destdir/anim.pak
$makepak $srcdir/chara_template/**/*.ron -o $destdir/chara_template.pak
$makepak $srcdir/deco/**/*.ron           -o $destdir/deco.pak
$makepak $srcdir/effect_img/**/*.ron     -o $destdir/effect_img.pak
$makepak $srcdir/item/**/*.ron           -o $destdir/item.pak
$makepak $srcdir/special_tile/**/*.ron   -o $destdir/special_tile.pak
$makepak $srcdir/tile/**/*.ron           -o $destdir/tile.pak
$makepak $srcdir/ui_img/**/*.ron         -o $destdir/ui_img.pak
$makepak $srcdir/wall/**/*.ron           -o $destdir/wall.pak
$makepak $srcdir/region_gen/**/*.ron     -o $destdir/region_gen.pak
$makepak $srcdir/script/**/*.py          -o $destdir/script.pak
$makepak $srcdir/site_gen/**/*.ron       -o $destdir/site_gen.pak

