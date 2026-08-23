import backend.core.unit_datasheet as unit_datasheet
from backend.cli.attack_seq import attack_phase

print("++ BEGIN ENCRYPTED MESSAGE ++")
print("|- BY AUTHORITY OF ARCHMAGOS SAF")
print("|")
print("|-P1: ULTRAMARINES")
print("|-P2: THOUSAND SONS CULTISTS")
first_attacker = input("|-Choose the attacker (1 or 2 only) \n")

if first_attacker == str(1):
    attacker = unit_datasheet.astartes_unit
    defender = unit_datasheet.ts_cult_unit

if first_attacker == str(2):
    attacker = unit_datasheet.ts_cult_unit
    defender = unit_datasheet.astartes_unit

while len(attacker['models']) > 0 and len(defender['models']) > 0:
    if len(defender['models']) == 0:
        print(f"\n🏆 {attacker['name']} has destroyed the enemy!\n")
        print(f"SUBMITTED TO ASTROPATHIC RELAY.")
        print(f"HAIL THE OMNISSIAH. HAIL THE MACHINE GOD.")
        break

    attack_phase(attacker, defender)
    attacker, defender = defender, attacker
    print("\n =====Swapping players...===== \n")