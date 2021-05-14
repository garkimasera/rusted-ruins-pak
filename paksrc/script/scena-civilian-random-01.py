# rusted-ruins-script

import rr
import random

def rr_main():
    n = random.randint(1, 2)
    text_talk_id = "{}-{:02}".format(rr.self_id(), n)
    yield ScriptYield.talk(text_talk_id)
    return
