# rusted-ruins-script

sid = game.self_id()

has_box = game.number_of_item("ancient-box") > 0

if game.vars["first-quest-received"] is None:
    response = game.talk(sid + "_before-first-quest", ["ans-yes", "ans-no"])
    if response == 0:
        game.talk(sid + "_first-quest-received")
        game.vars["first-quest-received"] = True
    else:
        game.talk(sid + "_first-quest-rejected")

elif game.vars["first-quest-cleared"] is None:
    if has_box:
        game.talk(sid + "_first-quest-received-with-box")
        game.vars["first-quest-cleared"] = True
        game.vars["given-box"] = 1
        game.remove_item("ancient-box", 1)
        game.receive_money(1000)
        game.receive_item("deed-of-land", 1)
        game.receive_item("building-hammer", 1)
        game.receive_item("lumberjack-axe", 1)
    else:
        game.talk(sid + "_first-quest-received-without-box")

elif has_box:
    game.vars["given-box"] += 1
    given_box = game.vars["given-box"]
    game.remove_item("ancient-box", 1)

    if given_box == 2:
        game.talk(sid + "_reward-01")
        game.receive_item("tricorder", 1)
    elif given_box == 4:
        game.talk(sid + "_reward-02")
        game.receive_item("skill-cartridge", 1)
    else:
        game.talk(sid + "_with-box")

    game.receive_money(2000)

else:
    game.talk(sid + "_without-box")
