import csv
import time

# Création de tuples pour chaque action - coùut de l'action - % profit depuis fichier csv
with open("data/dataset.csv", mode="r") as file:
	reader = csv.reader(file)
	next(reader)
	data = [tuple([row[0], int(row[1]), round((float(row[1]) * float(row[2]) / 100), 2)]) for row in reader]
print(data)


# Fonction force brute
def force_brute(maximum, actions, actions_selectionnees=[]):
	if actions:
		action = actions[0]
		profit_sans_action, liste_sans_action = force_brute(maximum, actions[1:], actions_selectionnees)
		if action[1] <= maximum:
			profit_avec_action, liste_avec_action = force_brute(maximum - action[1], actions[1:], actions_selectionnees + [action])
			if profit_sans_action < profit_avec_action:
				return profit_avec_action, liste_avec_action

		return profit_sans_action, liste_sans_action
	else:
		return sum([action[2] for action in actions_selectionnees]), actions_selectionnees


start = time.perf_counter()
print(force_brute(500, data))
stop = time.perf_counter()
print(stop-start)



