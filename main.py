import json
# Charger le JSON pour en faire un dictionnaire
with open('teams.json', 'r') as fcc_file:
    askbob_file = json.load(fcc_file)
    teams = askbob_file['data']
    parents_liste = [] # Liste de toutes les leagues (y compris vides)
    # Dédoublonner la liste des leagues
    for i in teams:
        parent = i['parent_team']
        if parent is not None:
            parent_nom = parent['code_name']
            parents_liste.append(parent_nom)
            parents_liste_unique = list(set(parents_liste))

    tribu_et_parent_liste = []
    tribu = []
    tribus_liste = []
    for fiche_octo in teams:
        tribu_nom = fiche_octo['code_name']
        tribu_parent_grappe = fiche_octo['parent_team']
        if tribu_parent_grappe is not None:
            tribu_parent_nom = tribu_parent_grappe['code_name']
            tribu_et_parent_liste.extend([tribu_parent_nom])
        else:
            parent = "Vide"
            tribu_et_parent_liste.extend(["Vide"])
        tribu.extend([tribu_nom])
        tribus_liste.extend([{"Tribu": tribu_nom, "Parent": tribu_parent_nom}])
        dict(tribus_liste)

    league_tribus_liste_unique = []
    for league in parents_liste_unique:
        liste_tribus_temp = []
        for fiche_octo_parent in tribus_liste:
            check_parent_tribe = fiche_octo_parent['Parent']
            if check_parent_tribe == league:
                liste_tribus_temp.append(fiche_octo_parent['Tribu'])
                tuple(liste_tribus_temp)
        league_tribus_liste_unique.extend([{"League": league,"Tribus": liste_tribus_temp}])
    league_tribus_liste_unique_json = json.dumps(league_tribus_liste_unique)
    #print(league_tribus_liste_unique_json)

    f = open('tribes.json', 'w')
    f.write(str(league_tribus_liste_unique_json))
    f.close()

    with open('tribes.json', 'r') as handle:
        parsed = json.load(handle)
        print(json.dumps(parsed, indent=4))

# [
#   {
#        "Name" : EVOLVE
#        "Tribus" : [
#                       { E-XVRS, CRAFT, ARCHI }
#                    ]
#    }
#]