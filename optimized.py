import csv
import time

FILE = "data/dataset2.csv"

# Création de tuples pour chaque action depuis fichier FILE: nom de l'action, coût de l'action, % profit
with open(FILE, mode="r") as file:
	reader = csv.reader(file)
	next(reader)

	# Non sélection des actions dont le montant est <= 0€ et profit <= 0% + passage en centimes
	data = []
	for row in reader:
		if float(row[1]) > 0:
			data.append(
				tuple([row[0], int(float(row[1]) * 100), float(row[1]) * float(row[2])]))


# Algorithme dynamique
def optimized(maximum, actions):
	"""

	Args:
		maximum (int): montant maximum
		actions (list): liste initiale de tuples (nom de l'aciton, prix de l'action, profit)

	Returns:
		combinaison générant le plus de profit (tuple): profit et actions sélectionnées

	"""

	matrice = [[0 for montant in range(maximum + 1)] for action in range(len(actions) + 1)]

	# axe y pour la liste des actions
	for y in range(1, len(actions) + 1):
		# axe x pour la liste des montants, 1 par 1
		for x in range(1, maximum + 1):
			# si le coût de l'action > montant
			if actions[y - 1][1] <= x:
				matrice[y][x] = max(actions[y - 1][2] + matrice[y - 1][x - actions[y - 1][1]], matrice[y - 1][x])
			else:
				matrice[y][x] = matrice[y - 1][x]

	# Retrouver les actions sélections en balayant en balayant la matrice en sens inverse
	n = len(actions)
	actions_selectionnees = []

	while maximum >= 0 and n >= 0:
		action = actions[n - 1]
		if matrice[n][maximum] == matrice[n - 1][maximum - action[1]] + action[2]:
			actions_selectionnees.append(action)
			maximum -= action[1]

		n -= 1

	return matrice[-1][-1], actions_selectionnees


def main():
	start = time.perf_counter()
	result = optimized(48924, data)
	stop = time.perf_counter()
	for action in result[1]:
		print(action[0])
	print(f"Profit max: {round(result[0] / 100, 2)}€")
	print(f"Somme dépensée: {sum([action[1]/100 for action in result[1]])}€")
	print(f"Temps de traitement: {round(stop - start, 2)}s")


main()
