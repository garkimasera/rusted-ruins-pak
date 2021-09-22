# rusted-ruins-script

import rr

def rr_main():
    sid = rr.self_id()

    if not rr.has_empty_for_party():
        yield ScriptYield.talk(sid + "-0")
        return
    
    yield ScriptYield.talk(sid + "-1", ["ans-yes", "ans-no"])
    if rr.response() == 0:
        rr.gen_party_chara("packhorse", 1)
        yield ScriptYield.talk(sid + "-2")
    else:
        yield ScriptYield.talk(sid + "-3")
