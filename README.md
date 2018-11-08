# Pak files for Rusted Ruins
This repository includes pak files, its image and source files, and translation files.

## How to compile

Please compile makepak binary first.

``` shell
git clone https://github.com/garkimasera/rusted-ruins.git
cd rusted-ruins/makepak
cargo install
```

And run build script.

``` shell
git clone https://github.com/garkimasera/rusted-ruins-pak.git
cd rusted-ruins-pak
./build.sh
```

## Create your own pak

For example, compiles one food item.

Prepare toml input file "my-super-ration.toml".

``` toml
object_type = "item"   # specify "item" to create item object
id = "my-super-ration" # object id
 
[image]
path = "my-super-ration.png" # Path to image file for this item
w = 24 # image width
h = 24 # image height

[item]
item_kind = "food" # item kind is food
gen_weight = 10    # generation weight in dungeons
gen_level = 0      # generation level in dungeons
basic_price = 5000 # item price
w = 10             # weight (gram)

nutrition = 1000   # nutrition of this item
```

Image file "my-super-ration.png" must be in the same directory. The image is displayed as this item.

You can compile this file by "rusted-ruins-makepak" command.

``` shell
rusted-ruins-makepak my-super-ration.toml -o mypak.pak
```

## License
CC BY 4.0
