# rusted-ruins-script

sid = game.self_id()

if not game.has_empty_for_party():
    game.talk(sid + "-0")
else:
    response = game.talk(sid + "-1", ["ans-yes", "ans-no"])
    if response == 0:
        game.gen_party_chara("packhorse", 1)
        game.talk(sid + "-2")
    else:
        game.talk(sid + "-3")
