import json

with open("askbob_people_withskills.json", 'r') as search:
    askbob_file = json.load(search)
    askbob_datas = askbob_file['data']

    askbob_skills_list = []
    askbob_skills_list = [{"Level": 1.0, "Trig": []}, {"Level": 2.0, "Trig": []}, {"Level": 3.0, "Trig": []}]

    for fiche_octo in askbob_datas:
        askbob_datas_trigram = fiche_octo['trigram']
        askbob_skills = fiche_octo['skills']

        for octo_skill in askbob_skills:
            if octo_skill is not None:
                askbob_skills_name = octo_skill['name']
                askbob_skills_level = octo_skill['level']

                if askbob_skills_name == "Python" and askbob_skills_level is not None:
                    if askbob_skills_level == askbob_skills_list[0]["Level"]:
                        askbob_skills_list[0]["Trig"].append(askbob_datas_trigram)
                    elif askbob_skills_level == askbob_skills_list[1]["Level"]:
                        askbob_skills_list[1]["Trig"].append(askbob_datas_trigram)
                    elif askbob_skills_level == askbob_skills_list[2]["Level"]:
                        askbob_skills_list[2]["Trig"].append(askbob_datas_trigram)

    list_json = json.dumps(askbob_skills_list)
    parsed = json.loads(list_json)
    print(json.dumps(parsed, indent=4))
