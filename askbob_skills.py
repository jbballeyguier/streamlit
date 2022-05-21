# 1) J'importe le fichier askbob
# 2) Je récupère la liste des skills et j'en fais un référentiel
# 3) Pour chaque skill, je boucle dans les fiches OCTO :
#   - J'identifie si l'OCTO a la skill et à quel niveau
#   - J'insère la skill et son niveau dans une variable

import json

with open("askbob_people_withskills.json", 'r') as search:
    askbob_file = json.load(search)
    askbob_datas = askbob_file['data']

    askbob_skills_list = []
    askbob_skills_name_list = []
    askbob_skills_list = [{"Level": 1.0, "Trig": []}, {"Level": 2.0, "Trig": []}, {"Level": 3.0, "Trig": []}]
    liste_skills = []

    for fiche_octo in askbob_datas:
        for skills in fiche_octo['skills']:
            skill = skills['name']
            if skill not in liste_skills:
                liste_skills.append(skill)
    #liste_skills_unique = list(set(liste_skills))

    template_skills_liste = []
    for skill_unique in liste_skills:
        template_skills_liste.append([{"Skill": skill_unique}, {"Levels": askbob_skills_list}])


    for fiche_octo in askbob_datas:
        askbob_datas_trigram = fiche_octo['trigram']
        askbob_skills = fiche_octo['skills']

        for octo_skill in askbob_skills:
            if octo_skill is not None:
                askbob_skills_name = octo_skill['name']
                askbob_skills_level = octo_skill['level']

                if askbob_skills_name in liste_skills and askbob_skills_level is not None:
                    if askbob_skills_level == askbob_skills_list[0]["Level"]:
                        template_skills_liste[1][0]["Trig"].append(askbob_datas_trigram)
                    elif askbob_skills_level == askbob_skills_list[1]["Level"]:
                        template_skills_liste[1][1]["Trig"].append(askbob_datas_trigram)
                    elif askbob_skills_level == askbob_skills_list[2]["Level"]:
                        template_skills_liste[1][2]["Trig"].append(askbob_datas_trigram)

    list_json = json.dumps(askbob_skills_name_list)
    parsed = json.loads(list_json)
    print(json.dumps(parsed, indent=4))
