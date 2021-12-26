# rusted-ruins-script

while True:
    response = game.talk(
        "guild_informant-start",
        [
            "guild_informant-ans-quest_offer",
            "guild_informant-ans-quest_report",
            "guild_informant-ans-add_dungeons",
            "guild_informant-ans-exit",
        ],
    )

    if response == 0:
        game.quest_offer()
    elif response == 1:
        game.quest_report()
    elif response == 2:
        var_name = "last-dungeon-location-update-time"
        update_time_exist = game.exist_gvar(var_name)
        before = game.get_gvar(var_name)
        current_time = game.current_time()

        if not update_time_exist or (current_time - before) > 24 * 30 * 3600:
            game.gen_dungeons()
            game.talk("guild_informant-after_add_dungeons")
            game.set_gvar(var_name, current_time)
        else:
            game.talk("guild_informant-add_dungeons_fail")
    else:
        break
