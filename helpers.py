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

def dmg_model(selected_model, defender, weapon):
        dead_flag = False
        selected_model["curr_w"] -= weapon["stats"]["D"]

        if selected_model["curr_w"] <= 0:
            defender["models"].remove(selected_model)
            dead_flag = True
            return dead_flag 
        else:
            dead_flag = False
            return dead_flag

def find_wounded(defender):
    for model in defender['models']:
        if model["curr_w"] < model["max_w"]:
            target_model = model
            return target_model
        
    return None
