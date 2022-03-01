# rusted-ruins-script

sid = game.self_id()

if game.skill_level("magic") == 0:
    response = game.talk(sid + "-00", ["ans-yes", "ans-no"])
    if response == 0:
        game.learn_skill("magic")
        game.learn_skill("heat")
        game.receive_item("ability-module-heat", 1)
        game.talk(sid + "-01")
    else:
        game.talk(sid + "-02")
else:
    game.talk(sid + "-03")
