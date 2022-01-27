import csv
import time

# Création de tuples pour chaque action depuis fichier csv: nom de l'action, coût de l'action, % profit
with open("data/dataset.csv", mode="r") as file:
	reader = csv.reader(file)
	next(reader)
	data = [tuple([row[0], int(row[1]), round((float(row[1]) * float(row[2]) / 100), 2)]) for row in reader]


# Fonction force brute, récursive, testant toutes les combinaisons possibles
def force_brute(maximum, actions, actions_selectionnees=[]):
	"""
	Args:
		maximum (int): montant maximum
		actions (list): liste initiale de tuples (nom de l'aciton, prix de l'action, profit)
		actions_selectionnees (list): liste finale d'actions sélectionnées

	Returns:
		combinaison générant le plus de profit (tuple): profit et actions sélectionnées
	"""
	if actions:
		action = actions[0]
		profit_sans_action, liste_sans_action = force_brute(maximum, actions[1:], actions_selectionnees)
		if action[1] <= maximum:
			profit_avec_action, liste_avec_action = \
				force_brute(maximum - action[1], actions[1:], actions_selectionnees + [action])
			if profit_sans_action < profit_avec_action:
				return profit_avec_action, liste_avec_action

		return profit_sans_action, liste_sans_action
	else:
		return sum([action[2] for action in actions_selectionnees]), actions_selectionnees


def main():
	start = time.perf_counter()
	result = force_brute(500, data)
	stop = time.perf_counter()
	for action in result[1]:
		print(action[0])
	print(f"Profit max: {round(result[0], 2)}€")
	print(f"Somme dépensée: {sum([action[1] for action in result[1]])}€")
	print(f"Temps de traitement: {round(stop-start, 2)}s")


main()
