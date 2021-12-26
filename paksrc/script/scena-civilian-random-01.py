# rusted-ruins-script

import random

n = random.randint(1, 2)
text_talk_id = "{}-{:02}".format(game.self_id(), n)
game.talk(text_talk_id)
