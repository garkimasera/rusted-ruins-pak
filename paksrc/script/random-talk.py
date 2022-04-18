# rusted-ruins-script
# id = "!random-talk"

import random

range = game.args["range"].split('..')
a = int(range[0])
b = int(range[1])

n = random.randint(a, b)
text_talk_id = "{}-{:02}".format(game.args["text_id"], n)
game.talk(text_talk_id)
