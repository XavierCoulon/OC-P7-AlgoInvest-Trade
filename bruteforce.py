import csv

# Create tuple for actions
with open("data/dataset.csv", mode="r") as file:
	reader = csv.reader(file)
	next(reader)
	test = [tuple([row[0], int(row[1]), round((float(row[1]) * float(row[2]) / 100), 2)]) for row in reader]
print(test)


def force_brute(maximum, actions, actions_selectionnees=[]):
	if actions:
		val1, lstval1 = force_brute(maximum, actions[1:], actions_selectionnees)
		val = actions[0]
		if val[1] <= maximum:
			val2, lstval2 = force_brute(maximum - val[1], actions[1:], actions_selectionnees + [val])
			if val1 < val2:
				return val2, lstval2

		return val1, lstval1
	else:
		return sum([action[2] for action in actions_selectionnees]), actions_selectionnees


print(force_brute(500, test))
