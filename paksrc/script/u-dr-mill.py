# rusted-ruins-script

sid = game.self_id()

if game.number_of_dead_party_members() > 0:
    response = game.talk(sid + "-00", ["ans-yes", "ans-no"])
    if response == 0:
        game.resurrect_party_members()
        game.talk(sid + "-01")
    else:
        game.talk(sid + "-02")
else:
    game.talk(sid + "-03")
