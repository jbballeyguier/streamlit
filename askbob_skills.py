# 1) J'importe le fichier askbob
# 2) Je récupère la liste des skills et j'en fais un référentiel
# 3) Pour chaque skill, je boucle dans les fiches OCTO :
#   - J'identifie si l'OCTO a la skill et à quel niveau
#   - J'insère la skill et son niveau dans une variable

import json

with open("askbob_people_withskills.json", 'r') as search:
    askbob_file = json.load(search)
    askbob_datas = askbob_file['data'] # Grappe des données askbob
    askbob_skills_ref = [] # Référentiel des compétences sous forme de liste itérable
    askbob_levels_trig = [[1.0, []], [2.0, []], [3.0, []]] # Liste des personnes par niveau d'une compétences entre 1 et 3
    template_skills_liste = []
    liste_skill_level_octo = []

# Je crée le référentiel des compétences à partir des données askbob
    for askbob_fiche_octo in askbob_datas:
        for skills in askbob_fiche_octo['skills']:
            skill = skills['name']
            if skill not in askbob_skills_ref:
                askbob_skills_ref.append(skill)
    askbob_skills_ref.sort()

# Je crée un template dans lequel je vais insérer les données

    for askbob_skill in askbob_skills_ref:
        template_skills_liste.append([askbob_skill, askbob_levels_trig])

    #print(template_skills_liste)
# Je parse le référentiel des compétences une par une et je regarde pour chaque fiche OCTO, si cette compétence existe et quel est son niveau

    for askbob_fiche_octo in askbob_datas:
        askbob_datas_trigram = askbob_fiche_octo['trigram']
        askbob_skills = askbob_fiche_octo['skills']


        for askbob_octo_skill in askbob_skills:
            liste_skill_level_octo.append([askbob_datas_trigram, askbob_skills_ref.index(askbob_octo_skill['name']), askbob_octo_skill['level']])

    for skill_octo in liste_skill_level_octo:
        trigram = skill_octo[0]
        skill_index = skill_octo[1]

        if skill_octo[2] == 1.0:
            level_index = 0
        elif skill_octo[2] == 2.0:
            level_index = 1
        elif skill_octo[2] == 3.0:
            level_index = 2

        #skills_liste_level = template_skills_liste[skill_index][1][level_index][1]
        tmp = []
        template_skills_liste[skill_index][1][level_index][1].append(trigram)

        tmp = template_skills_liste
        print(skill_index, level_index, template_skills_liste[skill_index][1][level_index][1])
        print(template_skills_liste[skill_index])
        #skills_liste_level.append(trigram)

#print(template_skills_liste)
f = open('skills.json', 'w')
f.write(str(template_skills_liste))
f.close()

    # list_json = json.dumps(template_skills_liste)
    # parsed = json.loads(list_json)
    # print(json.dumps(parsed, indent=4))