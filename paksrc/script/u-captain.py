# rusted-ruins-script

sid = game.self_id()

game.talk(sid + "-0")
response = game.talk(sid + "-1", ["ans-yes", "ans-no"])
if response == 0:
    game.talk(sid + "-2")
else:
    game.talk(sid + "-3")
