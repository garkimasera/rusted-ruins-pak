# rusted-ruins-script

import rr

def rr_main():
    while True:
        yield ScriptYield.talk(
            "shop-start", ["shop-ans-buy", "shop-ans-sell", "shop-ans-exit"]
        )
        choice = rr.response()
        if choice == 0:
            yield ScriptYield.shop_buy()
        elif choice == 1:
            yield ScriptYield.shop_sell()
        else:
            break
