#!/bin/bash

shopt -s globstar

for f in `ls ./**/*.toml`
do
    rusted-ruins-makepak $f -o /dev/null
done
