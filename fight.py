astartes_unit = {
    "name" : "Intercessor Squad",
    "M" : 6,
    "T" : 4,
    "SV": 3,
    "W" : 2,
    "LD": 6,
    "OC": 2,
    "keywords": ["INFANTRY", "BATTLELINE", "GRENADES", "IMPERIUM", "TACTICUS", "ASSAULT INTERCESSOR SQUAD"],
    "weapons": [
    {
        "name" :"Astartes chainsword",
        "A":4,
        "BS":3,
        "S":4,
        "AP":1,
        "D":1,
    },
    {
        "name": "Heavy bolt pistol",
        "A": 1,
        "BS": 3,
        "S": 4,
        "AP": 1,
        "D": 1,
    }]
}

ork_unit = {
    "name" : "BOY",
    "M" : 6,
    "T" : 5,
    "SV": 5,
    "W" : 1,
    "LD": 7,
    "OC": 2,
    "keywords": ["INFANTRY", "BATTLELINE", "MOB", "GRENADES", "BOYZ"],
    "weapons": [
    {
        "name" :"Choppa",
        "A":3,
        "BS":3,
        "S":4,
        "AP":1,
        "D":1,
    },
    {
        "name": "Big Shoota",
        "A": 3,
        "BS": 5,
        "S": 5,
        "AP": 0,
        "D": 1,
    }]

}

def calc_wound_value(weapon, defender):
    att_strength = weapon["S"]
    def_toughness = defender["T"]

    if att_strength >= def_toughness * 2:
        print("Need to roll a 2 or more to wound")
    elif att_strength * 2 < def_toughness:
              print("Need to roll a 6 or more to wound")  

    elif att_strength > def_toughness:
              print("Need to roll a 3 or more to wound")  
    elif att_strength == def_toughness:
              print("Need to roll a 4 or more to wound")  
    elif att_strength < def_toughness:
              print("Need to roll a 5 or more to wound")  
        
def calc_save_value(weapon, defender):
    def_save = defender["SV"]
    att_ap = weapon["AP"]

    save_value = def_save + att_ap
    print(f"Need to roll a {save_value} or more to save")
    
def calc_dmg(wound, save):
    total_wound = int(wound) - int(save)
    return total_wound

def attack_seq(attacker, defender):
    print("Which weapon to attack?")

    for index, weapon in enumerate(attacker["weapons"], start=1):
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
    calc_wound_value(selected_weapon, defender)
    print("How many successful wounds?")
    wound_dice = input("Wounds: ")

    print("-----SAVES-----")
    calc_save_value(selected_weapon, defender)
    print("Saves?")
    save_dice = input("Saves: ")


    total_wound = calc_dmg(wound_dice, save_dice)

    print("\n================ SUMMARY ================")
    print(f"{attacker['name']} attacks {defender['name']} with {selected_weapon['name']}!")
    print(f"• Hits: {hit_dice}")
    print(f"• Wounds: {wound_dice}")
    print(f"• Saves Passed: {save_dice}")
    print(f"• Total Damage Dealt: {selected_weapon['D']} Dmg per unsaved wound")
    print("=========================================")