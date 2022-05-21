test_dict1 = {"Name": "Jean-Baptiste", "Surname": "Balleyguier"}
test_dict2 = {"Name": "Gabrielle", "Surname": "Balleyguier"}
test_liste = [test_dict2, test_dict1]
test_nom = ["Jean-Baptiste", "Gabrielle", "Léon"]
test_tuple = ()

for Prenom in test_nom:
    for Name in test_liste:
        if Name['Name'] == Prenom:
            print(Prenom)