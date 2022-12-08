import random

# test_grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for row in test_grid:
    # print(row)
def Clean_boards():
		ship_board_1 = []
		for x in range(0,10):
			ship_board_1.append([])
			for y in range(0,10):
				ship_board_1[x].append(0)

def MarkAsOccupiedFromThisField(board, x, y):
	# temp = 1 + 3
	# print(temp)
	if (x - 1) > -1 and (y - 1) > -1:
		board[x-1][y-1] = 10
		
	if (x + 1) < 10 and (y - 1) > -1:
		board[x+1][y-1] = 10
	if (x + 1) < 10 and (y + 1) < 10:
		board[x+1][y+1] = 10
	if (x - 1) > -1 and (y + 1) < 10:
		board[x-1][y+1] = 10
    

def generate_ship(length, grid):
    # grid = []
    # for i in range(10):
    #     row = []
    #     for j in range(10):
    #         row.append(0)
    #     grid.append(row)
    
    # randomly pick a starting point and a direction
    not_colliding = False
    while not_colliding is False:
        random_x = random.randint(0, 9)
        random_y = random.randint(0, 9)
        direction = random.randint(0, 1)  # 0 for horizontal, 1 for vertical
        
        # check if the ship will fit on the grid
        if direction == 0:
            # check if the ship fits horizontally
            if random_y + length > 10:
            # the ship won't fit, so pick a new starting point
                random_y = random.randint(0, 9 - length)
        elif direction == 1:
            # check if the ship fits vertically
            if random_x + length > 10:
            # the ship won't fit, so pick a new starting point
                random_x = random.randint(0, 9 - length)

        # check if the ship will not collide with others ships
        if direction == 0:
            for i in range(length):
                if grid[random_x][random_y + i] == 3 or grid[random_x][random_y + i] == 10:
                    # print("nie miesci sie")
                    return False
                else: not_colliding = True
        elif direction == 1:
            for i in range(length):
                if grid[random_x + i][random_y] == 3 or grid[random_x + i][random_y] == 10:
                    # print("nie miesci sie")
                    return False
                else: not_colliding = True   

    # place the ship on the grid
    for i in range(length):
        if direction == 0:
        # place the ship horizontally
            if i == 0 and random_y - 1 > -1: # add restricion on start of ships
                # print("dodano gorne")
                grid[random_x][random_y - 1] = 10
            if i == length - 1 and random_y + 1 + i < 10: # add restricion on end of ships
                # print("dodano dolne")
                grid[random_x][random_y + i + 1] = 10
            grid[random_x][random_y + i] = 3
            MarkAsOccupiedFromThisField(test_grid, random_x, random_y + i)
        else:
        # place the ship vertically
            if i == 0 and random_x - 1 > -1: # add restricion on start of ships
                # print("dodano gorne")
                grid[random_x - 1][random_y] = 10
            if i == length - 1 and random_x + 1 + i < 10: # add restricion on end of ships
                # print("dodano dolne")
                # print(random_x + i + 1)
                grid[random_x + i + 1][random_y] = 10
            grid[random_x + i][random_y] = 3
            MarkAsOccupiedFromThisField(test_grid, random_x + i, random_y)
    
    # print(grid)
    return grid

ships_1 = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
counter = 0
while counter != 20:
    counter = 0
    placement_loop = False
    while placement_loop is False:
        can_fit = True
        test_grid = []
        for x in range(0,10):
            test_grid.append([])
            for y in range(0,10):
                test_grid[x].append(0)
        for i in range(len(ships_1)):
            tester = generate_ship(ships_1[i], test_grid)
            if tester == False: # jeżeli jakaś funkcja nie była w stanie postawić statku to zwróci Fakse który musimy przechować przez całego for'a
                can_fit = tester # zmieniamy went_wrong z True na False żeby pętla nam się
            # print(ships_1[i])
            placement_loop = can_fit
    for x in range(0,10):
        for y in range(0,10):
            if test_grid[x][y] == 3:
                counter += 1
        
# generate_ship(4,test_grid)

for row in test_grid:
    print(row)
counter_2 = 0
# while counter != 20:
#     # counter = 0
for x in range(0,10):
    for y in range(0,10):
        if test_grid[x][y] == 3:
            counter_2 += 1

print(counter_2)
       
    