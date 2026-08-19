import helpers

def attack_phase(attacker, defender):
    weapon_grp = helpers.get_weapons(attacker)

    for weapon,data in weapon_grp.items():
        print(f"\n-----{data["stats"]["name"].upper()} HITS-----")
        a_stat = data["stats"]["A"]
        a_stat *= data["count"]
        print(f"Roll {a_stat} dice for {weapon} ({data["stats"]["BS"]} or more for success hit)")

        valid_a = False
        while valid_a is False:
            succ_a = input("Successful attack: ")
            valid_a = helpers.input_validator(a_stat, int(succ_a))

            if valid_a is True:
               break
            elif valid_a is False:
                print("Invalid input try again\n")


        if int(succ_a) > 0:
            print(f"\n-----{data["stats"]["name"].upper()} WOUNDS-----")
            w_value = helpers.calc_wound_value(data,defender)
            print(f"Roll {succ_a} dice for {weapon} ({w_value} or more for success wound)")

            valid_w = False
            while valid_w is False:
                succ_w = input("Successful wound: ")
                valid_w = helpers.input_validator(int(succ_a), int(succ_w))
                if valid_w is True:
                    break
                elif valid_w is False:
                    print("Invalid input try again\n")


            if int(succ_w) > 0:
                print(f"\n-----{data["stats"]["name"].upper()} SAVES-----")
                sv_value = helpers.calc_save_value(data, defender)
                print(f"Roll {succ_w} dice to save from {weapon} ({sv_value} or more for success save)")

                valid_sv = False
                while valid_sv is False:
                    succ_sv = input("Successful save: ")
                    valid_sv = helpers.input_validator(sv_value, int(succ_sv))
                    if valid_sv is True:
                        break
                    elif valid_sv is False:
                        print("Invalid input try again\n")
                        
                fail_sv = int(succ_w) - int(succ_sv)

                for fail in range(fail_sv):
                    damaged_model  = helpers.find_wounded(defender)
                    if damaged_model is not None:
                        print(f"{damaged_model['name']} is already damaged [{damaged_model['curr_w']}/{damaged_model['max_w']} HP]. Allocating damage..")
                        selected_model = damaged_model
                    else:
                        print("\n =====CHOOSE MODEL TO BE DAMAGED=====")
                        for index, model in enumerate(defender["models"]):
                            print(f"{index}. {model['name']} [{model['curr_w']} HP]")

                        valid_model = False
                        while valid_model is False: 
                            model_index = input("Unit to damage (numbers only): ")
                            valid_model = helpers.input_validator(len(defender['models']), int(model_index))
                            if valid_model is False:
                                print("Invalid input try again\n")
                            else:
                                break
  
                        selected_model = defender['models'][int(model_index)] 

                    result = helpers.dmg_model(selected_model, defender, data)

                    if result is False:
                        print(f"\n{selected_model['name']} took damage! [{selected_model['curr_w']} HP left]")
                    elif result is True:
                        print(f"XX {selected_model['name']} is dead. XX")
                else:
                    continue

        else:
            print("\n =====End of attack sequence===== \n")

