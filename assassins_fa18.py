#Original program written by Kelly Hong. Adapted to committee assassins by Peter Ren.

import random
import os
import os.path


#NOTE: This may also be implemented (and more efficiently) using a tuple instead of defining an extra class.

class Pairing:
	def __init__(self, key, value):
		self.key = key
		self.value = value

arr = ['CS', 'SoComm', 'Historian', 'Design', 'Culture']
prev_pairings = []
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
d = 0
while(d < 5):
	random.shuffle(arr)
	killer_victim = {}
	for i in range(len(arr)):
		killer = arr[i]
		if i + 1 == len(arr):
			killer_victim[killer] = arr[0]
		else:
			killer_victim[killer] = arr[i + 1]
	already_exists = False
	for killer in killer_victim:
		for pairing in prev_pairings:
			if pairing.key == killer and pairing.value == killer_victim[killer]:
				already_exists = True
	if not already_exists:
		os.mkdir(days[d])
		original_directory = os.getcwd()
		os.chdir(days[d])
		for killer in killer_victim:
			print("entered_file_creation_loop")
			prev_pairings.append(Pairing(killer, killer_victim[killer]))
			os.mkdir(killer)
			file_name = os.path.join(killer, killer + "_victim.txt")
			file1 = open(file_name, "w")
			file1.write(killer_victim[killer])
			file1.close()
		os.chdir(original_directory)
		d += 1
