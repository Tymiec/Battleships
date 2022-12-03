import random

plansza_trafien_1 = []
plansza_trafien_2 = []
plansza_statkow_1 = []
plansza_statkow_2 = []

place_player_ship_counter = 0
for x in range(0,10):
	plansza_trafien_1.append([])
	plansza_trafien_2.append([])

	plansza_statkow_1.append([])
	plansza_statkow_2.append([])
	for y in range(0,10):
		plansza_trafien_1[x].append(0)
		plansza_trafien_2[x].append(0)

		plansza_statkow_1[x].append(0)
		plansza_statkow_2[x].append(0)

statki = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

for z in range(len(statki)):
	random_x = -1
	random_y = -1
	print(f"x:{z}")
	print(f"Ship length: {statki[z]}")

	not_different = True
	while not_different: # random generating coordinate until we find a free spot
		random_x = random.randint(0,9)
		random_y = random.randint(0,9)
		if plansza_statkow_2[random_x][random_y] != 3 and plansza_statkow_2[random_x][random_y] != 2:
			not_different = False

	print(f"Coordinates: {random_x}, {random_y}")
	if plansza_statkow_2[random_x][random_y] != 3 and plansza_statkow_2[random_x][random_y] != 2: # sprawdzamy czy nie stawiamy na statku albo obok
		plansza_statkow_2[random_x][random_y] = 3 #dodajemy statek			
		print(f"Generating computer ship no {z}\n")
		length_of_ship = statki[z]
		for i in range(length_of_ship-1):
			not_generated = True
			while not_generated:
				direction = random.randint(0,3) # 0 = GÓRA 1 = PRAWO 2 = DÓŁ 3 = LEWO
				if direction == 0:
					if plansza_statkow_2[random_x][random_y + 1] != 3 and plansza_statkow_2[random_x][random_y + 1] != 2:
						random_y += 1
					else: direction +=1

				elif direction == 1:
					if plansza_statkow_2[random_x + 1][random_y] != 3 and plansza_statkow_2[random_x + 1][random_y] != 2:
						random_x += 1
					else: direction += 1

				elif direction == 2:
					if plansza_statkow_2[random_x][random_y - 1] != 3 and plansza_statkow_2[random_x][random_y - 1] != 2:
						random_y -= 1
					else: direction -= 1
				
				elif direction == 3:
					if plansza_statkow_2[random_x + 1][random_y] != 3 and plansza_statkow_2[random_x + 1][random_y] != 2:
						random_x -= 1	
					else: direction = 0	
	# 		print("EZ")
	# 	# 	print(plansza_statkow_2)

            # [[0, 0, 0, 0, 3, 0, 0, 0, 0, 0], 
            # [0, 0, 0, 0, 0, 0, 0, 0, 0, 3], 
            # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            # [0, 0, 0, 0, 0, 0, 0, 0, 3, 0], 
            # [0, 0, 0, 0, 0, 0, 3, 0, 0, 0], 
            # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            # [0, 0, 0, 0, 3, 0, 0, 0, 0, 0], 
            # [0, 0, 0, 0, 0, 0, 0, 0, 0, 3], 
            # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
            # [0, 0, 3, 0, 3, 3, 0, 3, 0, 0]]