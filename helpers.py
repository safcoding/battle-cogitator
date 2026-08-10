from weapon_datasheet import weapons

def get_weapons(attacker):
    weapon_grp = {}
    
    for model in attacker["models"]:
        ranged_weapon = model.get("r_weapon")

        if not ranged_weapon or ranged_weapon == "none":
            continue

        if ranged_weapon in weapon_grp:
            weapon_grp[ranged_weapon]["count"] += 1
        else:
            weapon_grp[ranged_weapon] = {
                "count": 1,
                "stats": weapons[ranged_weapon]
            }
    return weapon_grp

def calc_wound_value(weapon, defender):
    att_strength = weapon["stats"]["S"]
    def_toughness = defender["T"]

    if att_strength >= def_toughness * 2:
        return 2
    elif att_strength * 2 < def_toughness:
        return 6
    elif att_strength > def_toughness:
        return 3
    elif att_strength == def_toughness:
        return 4
    elif att_strength < def_toughness:
        return 5  
        
def calc_save_value(weapon, defender):
    att_ap = weapon["stats"]["AP"]
    def_save = defender["SV"]

    save_value = def_save + att_ap
    return save_value

def dmg_model(fail_sv, defender, weapon):
    for fail in range(fail_sv):
        if len(defender["models"]) == 0:
            print("unit is dead")
            break

        target_model = None

        for model in defender['models']:
            if model["curr_w"] < model["max_w"]:
                target_model = model
                print(f"{model['name']} is already damaged [{model['curr_w']} HP]. Allocating damage to {model['name']}")
                break

        if target_model is None:
            print("\n =====CHOOSE MODEL TO BE DAMAGED=====")
            for index, model in enumerate(defender["models"]):
                print(f"{index}. {model['name']} [{model['curr_w']} HP]")

            selected_model = input("Unit to damage (numbers only): ")
            target_model = defender["models"][int(selected_model)]

        target_model["curr_w"] -= weapon["stats"]["D"]
        print(f"\n{target_model['name']} took damage! [{target_model['curr_w']} HP left]")

        if target_model["curr_w"] <= 0:
            print(f"XX {target_model['name']} is dead. XX")
            defender["models"].remove(target_model)
