# rusted-ruins-script

while True:
    response = game.talk("shop-start", ["shop-ans-buy", "shop-ans-sell", "shop-ans-exit"])
    if response == 0:
        game.shop_buy()
    elif response == 1:
        game.shop_sell()
    else:
        break
