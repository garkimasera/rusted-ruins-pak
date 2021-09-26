# rusted-ruins-script

import rr

def rr_main():
    sid = rr.self_id()

    if rr.number_of_dead_party_members() > 0:
        yield ScriptYield.talk(sid + "-00", ["ans-yes", "ans-no"])
        if rr.response() == 0:
            rr.resurrect_party_members()
            yield ScriptYield.talk(sid + "-01")
        else:
            yield ScriptYield.talk(sid + "-02")
    else:
        yield ScriptYield.talk(sid + "-03")
