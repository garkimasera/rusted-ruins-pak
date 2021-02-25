# rusted-ruins-script

import rr


def rr_main():
    sid = rr.self_id()

    yield ScriptYield.talk(sid + "-0")
    yield ScriptYield.talk(sid + "-1", ["ans-yes", "ans-no"])
    if rr.yield_result() == 0:
        yield ScriptYield.talk(sid + "-2")
    else:
        yield ScriptYield.talk(sid + "-3")
