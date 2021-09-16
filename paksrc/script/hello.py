# rusted-ruins-script

import rr


def rr_main():
    while True:
        yield ScriptYield.talk("hello-start")
        yield ScriptYield.talk("hello-next", ["ans-yes", "ans-no"])
        if rr.response() == 1:
            break
    return
