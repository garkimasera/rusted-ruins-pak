# rusted-ruins-script

import rr


def rr_main():
    sid = rr.self_id()

    if not rr.exist_var("first-quest-received"):
        yield ScriptYield.talk(sid + "_before-first-quest", ["ans-yes", "ans-no"])
        if rr.yield_result() == 0:
            yield ScriptYield.talk(sid + "_first-quest-received")
            rr.set_var("first-quest-received", True)
            return
        else:
            yield ScriptYield.talk(sid + "_first-quest-rejected")
            return

    has_box = rr.has_item("ancient-box") > 0

    if not rr.exist_var("first-quest-cleared"):
        if has_box:
            yield ScriptYield.talk(sid + "_first-quest-received-with-box")
            rr.set_var("first-quest-cleared", True)
            rr.set_var("given-box", 1)
            rr.remove_item("ancient-box", 1)
            rr.receive_money(1000)
            rr.receive_item("deed-of-land", 1)
            rr.receive_item("building-hammer", 1)
            rr.receive_item("lumberjack-axe", 1)
            return
        else:
            yield ScriptYield.talk(sid + "_first-quest-received-without-box")
            return

    if has_box:
        given_box = rr.get_var("given-box") + 1
        rr.set_var("given-box", given_box)
        rr.remove_item("ancient-box", 1)

        if given_box == 2:
            yield ScriptYield.talk(sid + "_reward-01")
            rr.receive_item("tricorder", 1)
        elif given_box == 4:
            yield ScriptYield.talk(sid + "_reward-02")
            rr.receive_item("skill-cartridge", 1)
        else:
            yield ScriptYield.talk(sid + "_with-box")

        rr.receive_money(2000)
        return

    yield ScriptYield.talk(sid + "_without-box")
