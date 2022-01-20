import csv
import time

# Création de tuples pour chaque action - coùut de l'action - % profit depuis fichier csv
with open("data/dataset1_test.csv", mode="r") as file:
	reader = csv.reader(file)
	next(reader)

	# for i in reader:
	#	print(round(float(i[1])*100, 0))

	# Pour dataset1 et 2
	data = [tuple([row[0], round(int(float(row[1])*100), 0), int(round((float(row[1]) * float(row[2]) / 100), 2)*100)]) for row in reader if round(int(float(row[1])*100), 0) > 0]

	# Pour dataset
	# data = [tuple([row[0], int(row[1]), round((float(row[1]) * float(row[2]) / 100), 2)]) for row in reader]

	# print(data)


# Aglo dynamique
def dynamique(maximum, actions):
	matrice = [[0 for x in range(maximum + 1)] for x in range(len(actions) + 1)]

	for i in range(1, len(actions) + 1):
		for w in range(1, maximum + 1):
			if actions[i-1][1] <= w:
				matrice[i][w] = max(actions[i-1][2] + matrice[i-1][w-actions[i-1][1]], matrice[i-1][w])
			else:
				matrice[i][w] = matrice[i-1][w]

	# Retrouver les éléments en fonction de la somme
	w = maximum
	n = len(actions)
	actions_selectionnees = []

	while w >= 0 and n >= 0:
		e = actions[n-1]
		if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
			actions_selectionnees.append(e)
			w -= e[1]

		n -= 1

	return matrice[-1][-1], actions_selectionnees


start = time.perf_counter()
print(dynamique(50000, data))
stop = time.perf_counter()
print(stop-start)