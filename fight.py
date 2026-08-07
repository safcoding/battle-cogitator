import unit_datasheet
import helpers

def attack_seq(attacker, defender):
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

        seq_log.append(f"x{succ_sv} saves from {data["stats"]["name"]}")
        seq_log.append(f"x{succ_w} {data["stats"]["D"]} damage from {data["stats"]["name"]}")

    print("\n================ SUMMARY ================")
    for line in seq_log:
        print(line)
    print("End of attack sequence")

attack_seq(unit_datasheet.astartes_unit, unit_datasheet.khorne_unit)


"""
def attack_seq(attacker, defender):
    print("Which weapon to attack?")

    for index, weapon in enumerate(attacker["models"[index]], start=1):
        print(f"{index}. { weapon['name']}")

    choice = input("Selected weapon: ")
    weapon_index = int(choice) - 1

    selected_weapon = attacker['weapons'][weapon_index]
    print(f"Attacking with {selected_weapon['name']}!")

    print("-----HITS-----")
    print(f"Roll {selected_weapon['A']} dice(s)")
    print(f"How many successful hits? (Dice more or equal to {selected_weapon['BS']})")
    hit_dice = input("Hits: ")

    print("-----WOUNDS-----")
    helpers.calc_wound_value(selected_weapon, defender)
    print("How many successful wounds?")
    wound_dice = input("Wounds: ")

    print("-----SAVES-----")
    helpers.calc_save_value(selected_weapon, defender)
    print("Saves?")
    save_dice = input("Saves: ")

    print("\n================ SUMMARY ================")
    print(f"{attacker['name']} attacks {defender['name']} with {selected_weapon['name']}!")
    print(f"• Hits: {hit_dice}")
    print(f"• Wounds: {wound_dice}")
    print(f"• Saves Passed: {save_dice}")
    print(f"• Total Damage Dealt: {selected_weapon['D']} Dmg per unsaved wound")
    print("=========================================")

attack_seq(datasheet.astartes_unit, datasheet.khorne_unit)
"""