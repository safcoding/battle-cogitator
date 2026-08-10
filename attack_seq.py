import helpers

def attack_phase(attacker, defender):
    weapon_grp = helpers.get_weapons(attacker)
    seq_log = []

    for weapon,data in weapon_grp.items():
        print(f"\n-----{data["stats"]["name"].upper()} HITS-----")
        a_stat = data["stats"]["A"]
        a_stat *= data["count"]
        print(f"Roll {a_stat} dice for {weapon} ({data["stats"]["BS"]} or more for success hit)")

        succ_a = input("Successful attack: ")

        print(f"\n-----{data["stats"]["name"].upper()} WOUNDS-----")
        w_value = helpers.calc_wound_value(data,defender)
        print(f"Roll {succ_a} dice for {weapon} ({w_value} or more for success wound)")

        succ_w = input("Successful wound: ")

        print(f"\n-----{data["stats"]["name"].upper()} SAVES-----")
        sv_value = helpers.calc_save_value(data, defender)
        print(f"Roll {succ_w} dice to save from {weapon} ({sv_value} or more for success save)")

        succ_sv = input("Successful save: ")
        fail_sv = int(succ_w) - int(succ_sv)
        helpers.dmg_model(fail_sv, defender, data)

        if len(defender['models']) == 0:
            print(f"\n🏆 {attacker['name']} has destroyed the enemy! Game Over!")
            break

        seq_log.append(f"x{succ_sv} saves from {data["stats"]["name"]}")
        seq_log.append(f"x{succ_w} {data["stats"]["D"]} damage from {data["stats"]["name"]}")

    print("\n================ SUMMARY ================")
    for line in seq_log:
        print(line)
    print("End of attack sequence\n")

