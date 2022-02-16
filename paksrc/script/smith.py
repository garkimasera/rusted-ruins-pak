# rusted-ruins-script

while True:
    response = game.talk(
        "smith-start",
        ["shop-ans-buy", "smith-ans-ability-slot", "smith-ans-extend-slot", "shop-ans-exit"])
    if response == 0:
        game.shop_buy()
    elif response == 1:
        game.install_ability_slot()
    elif response == 2:
        game.install_extend_slot()
    else:
        break
