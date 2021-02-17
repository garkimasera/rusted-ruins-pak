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

```shell
git clone https://github.com/garkimasera/rusted-ruins-pak.git
cd rusted-ruins-pak
./build.sh
```

## Create your own pak

For example, compiles one food item.

Prepare toml input file "my-super-ration.ron".

```ron
(
    object_type: "item", // specify "item" to create item object
    id: "my-super-ration", // object id
    
    image: (
        copyright: "...",
        path: "my-super-ration.png", // Path to image file for this item
    ),
    
    item: (
        item_kind: "food",         // item kind is food
        group: "preserved-food",   // item group name
        gen_weight: 10,            // generation weight in dungeons
        shop_weight: 10,           // generation weight in shops
        gen_level: 1,              // generation level in dungeons
        basic_price: 500,          // item price
        w: 10,                    // weight (gram)
        attrs: [
            Nutrition(1000),       // Nutrition of this item
        ],
    ),
)
```

Image file "my-super-ration.png" must be in the same directory. The image is displayed as this item.

You can compile this file by "rusted-ruins-makepak" command.

``` shell
rusted-ruins-makepak my-super-ration.toml -o mypak.pak
```

## License
CC BY 4.0
