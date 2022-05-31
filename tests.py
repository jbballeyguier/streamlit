test_dict1 = ["Valeur 1", [1, 2]]
test_dict2 = ["Valeur 2", [2, 3]]
test_liste = [test_dict1, test_dict2]
test_nom = [0, 1]
test_tuple = ()

for i in test_nom:
    test_liste[test_nom.index(i)][1].append(i)

print(test_liste)