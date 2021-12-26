# rusted-ruins-script

sid = game.self_id()

has_box = game.number_of_item("ancient-box") > 0

if not game.exist_var("first-quest-received"):
    response = game.talk(sid + "_before-first-quest", ["ans-yes", "ans-no"])
    if response == 0:
        game.talk(sid + "_first-quest-received")
        game.set_var("first-quest-received", True)
    else:
        game.talk(sid + "_first-quest-rejected")

elif not game.exist_var("first-quest-cleared"):
    if has_box:
        game.talk(sid + "_first-quest-received-with-box")
        game.set_var("first-quest-cleared", True)
        game.set_var("given-box", 1)
        game.remove_item("ancient-box", 1)
        game.receive_money(1000)
        game.receive_item("deed-of-land", 1)
        game.receive_item("building-hammer", 1)
        game.receive_item("lumberjack-axe", 1)
    else:
        game.talk(sid + "_first-quest-received-without-box")

elif has_box:
    given_box = game.get_var("given-box") + 1
    game.set_var("given-box", given_box)
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
