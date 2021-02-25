# rusted-ruins-script


def rr_main():
    while True:
        yield ScriptYield.talk(
            "shop-start", ["shop-ans-buy", "shop-ans-sell", "shop-ans-exit"]
        )
        c = last_choice()
        if c == 0:
            yield ScriptYield.shop_buy()
        elif c == 1:
            yield ScriptYield.shop_sell()
        else:
            break
