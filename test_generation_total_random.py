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

for x in range(20):
	not_different = True
	while not_different: # random generating coordinate until we find a free spot
		random_x = random.randint(0,9)
		random_y = random.randint(0,9)
		if plansza_statkow_2[random_x][random_y] != 3 and plansza_statkow_2[random_x][random_y] != 2:
			not_different = False
	if plansza_statkow_2[random_x][random_y] != 3: # sprawdzamy czy nie stawiamy na statku FIXME: chyba zbędny?
		plansza_statkow_2[random_x][random_y] = 3 #dodajemy statek		
		print(f"pepega {x}")

print(plansza_statkow_2)