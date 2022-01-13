# rusted-ruins-script

sid = game.self_id()
quest_id = sid + "-packhorse"

if game.custom_quest_completed(quest_id):
    game.talk(sid + "-08")

elif not game.custom_quest_started(quest_id):
    response = game.talk(sid + "-01", ["ans-take", "ans-goodbye"])
    if response == 0:
        game.start_custom_quest(quest_id, "start")
        game.talk(sid + "-02")

else:
    response = game.talk(sid + "-03", ["ans-yes", "ans-no"])
    if response == 0:
        if game.number_of_item("wood") >= 10:
            if game.has_empty_for_party:
                game.talk(sid + "-04")
                game.remove_item("wood", 10)
                game.gen_party_chara("packhorse", 1)
                game.complete_custom_quest(quest_id)
            else:
                game.talk(sid + "-07")
        else:
            game.talk(sid + "-06")
    else:
        game.talk(sid + "-05")
