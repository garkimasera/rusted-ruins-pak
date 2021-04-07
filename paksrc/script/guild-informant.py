# rusted-ruins-script

import rr


def rr_main():
    while True:
        yield ScriptYield.talk(
            "guild_informant-start",
            [
                "guild_informant-ans-quest",
                "guild_informant-ans-reward",
                "guild_informant-ans-add_dungeons",
                "guild_informant-ans-exit",
            ],
        )
        last_choice = rr.yield_result()
        if last_choice == 0:
            yield ScriptYield.quest()
        elif last_choice == 1:
            if rr.receive_quest_rewards():
                yield ScriptYield.talk("guild_informant-reward_recieved")
            else:
                yield ScriptYield.talk("guild_informant-reward_not_recieved")
        elif last_choice == 2:
            var_name = "last-dungeon-location-update-time"
            update_time_exist = rr.exist_gvar(var_name)
            before = rr.get_gvar(var_name)
            current_time = rr.current_time()

            if not update_time_exist or (current_time - before) > 24 * 30 * 3600:
                rr.gen_dungeons()
                yield ScriptYield.talk("guild_informant-after_add_dungeons")
                rr.set_gvar(var_name, current_time)
            else:
                yield ScriptYield.talk("guild_informant-add_dungeons_fail")
        else:
            break
