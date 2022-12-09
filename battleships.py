import random
import pygame
from pygame.locals import *
from random import randrange
import pygame, sys
from pygame.locals import *
import button
##
# EXISITING BUGS:
# dynamic button scaling does not work
# you can't clear the generated player board because it fills but going back and generating it again does the trick
##

class Battleships():
	
	def __init__(self):

		self.fps = 60
		frame_height = 224
		# self.frame_scale = 16/9
		self.frame_scale = 1.142857142857143
		
		# COORDIANTES OF LEFT CORNER OF BOARD_1
		# X: 66 Y: 258 every move by x: 38 i y: 38
		# COORDIANTES OF LEFT CORNER OF BOARD_2
		# X: 578 Y: 258 every move by x: 38 i y: 38

		pygame.init()

		current_screen = pygame.display.Info()
		i = 1

		# while frame_height * i < current_screen.current_h * 0.8 :
		# 	i += 1

		frame_height = 896


		pygame.mixer.init()

		self.game_clock = pygame.time.Clock()
		self.this_windows = pygame.display.set_mode((int(frame_height * i * self.frame_scale), frame_height * i), HWSURFACE|DOUBLEBUF|RESIZABLE)
		icon = pygame.image.load("Assets/Images/icon.png")

		pygame.display.set_icon(icon)
		pygame.display.set_caption("BATTLESHIPS")

		self.obraz = pygame.surface.Surface(self.this_windows.get_rect().size)
		self.obraz.fill((0, 0, 0))

		####################################################### LOADERS #######################################################
		self.music = [
			"Assets/Sound/bitwa_shanty_nes_by_kimel.ogg",
			"Assets/Sound/wellerman_8bit_midi_by_kimel.ogg",
			"Assets/Sound/wellerman_8bit_midi_by_kimel_35plus.ogg"
		]

		# INTRO LOADER
		self.introSprite = pygame.image.load("Assets/Images/intro_sprite.png")

		# MENU LOADER
		self.menu_backgrund = pygame.image.load("Assets/Images/menu.png")
		self.preparation_background = pygame.image.load("Assets/Images/preparation_screen.png")
		self.end_background = pygame.image.load("Assets/Images/end_screen.png")
		self.numbers = pygame.image.load("Assets/Images/numbers_sprite.png")
		self.credits = pygame.image.load("Assets/Images/credits.png")

		# OPTIONS LOADER
		self.options = pygame.image.load("Assets/Images/options.png")

		# BUTTON LOADER
		self.play_no_hover = pygame.image.load("Assets/Images/play_no_hover.png").convert_alpha()
		self.play_hover = pygame.image.load("Assets/Images/play_hover.png").convert_alpha()
		self.play_button = button.Button(398, 385, self.play_no_hover, self.play_hover, 1)

		self.start_no_hover = pygame.image.load("Assets/Images/start_no_hover.png").convert_alpha()
		self.start_hover = pygame.image.load("Assets/Images/start_hover.png").convert_alpha()
		self.start_button = button.Button(369, 680, self.start_no_hover, self.start_hover, 1)

		self.options_no_hover = pygame.image.load("Assets/Images/options_no_hover.png").convert_alpha()
		self.options_hover = pygame.image.load("Assets/Images/options_hover.png").convert_alpha()
		self.options_button = button.Button(319, 485, self.options_no_hover, self.options_hover, 1)

		self.credits_no_hover = pygame.image.load("Assets/Images/credits_no_hover.png").convert_alpha()
		self.credits_hover = pygame.image.load("Assets/Images/credits_hover.png").convert_alpha()
		self.credits_button = button.Button(319, 585, self.credits_no_hover, self.credits_hover, 1)

		self.exit_no_hover = pygame.image.load("Assets/Images/exit_no_hover.png").convert_alpha()
		self.exit_hover = pygame.image.load("Assets/Images/exit_hover.png").convert_alpha()
		self.exit_button = button.Button(408, 825, self.exit_no_hover, self.exit_hover, 1)

		self.x_back_button = 20
		self.y_back_button = 20
		self.back_no_hover = pygame.image.load("Assets/Images/back_no_hover.png").convert_alpha()
		self.back_hover = pygame.image.load("Assets/Images/back_hover.png").convert_alpha()
		self.back_button = button.Button(self.x_back_button, self.y_back_button, self.back_no_hover, self.back_hover, 0.4)

		self.generate_no_hover = pygame.image.load("Assets/Images/generate_no_hover.png").convert_alpha()
		self.generate_hover = pygame.image.load("Assets/Images/generate_hover.png").convert_alpha()
		self.generate_button = button.Button(116, 122, self.generate_no_hover, self.generate_hover, 1)
		# 50 i -136
		# GAME LOADERS
		self.hit_sprite = pygame.image.load("Assets/Images/hit_sprite.png").convert_alpha()
		self.aim = pygame.image.load('C:/Repo/Battleshipz/Assets/Images/aim.png').convert_alpha()

		self.player_move = False
		self.computer_move = False
		
		self.selected_song = 0
		self.place_player_ship_counter = 0
		self.generation_counter = 0
		self.generation_counter_2 = 0
		self.player_shot_counter = 0
		self.computer_shot_counter = 0
		self.player_succesfull_hit_counter = 0
		self.computer_succesfull_hit_counter = 0
		self.player_shot_counter_array = []
		self.computer_shot_counter_array = []
		self.player_succesfull_hit_counter_array = []
		self.computer_succesfull_hit_counter_array = []

		self.hit_board_1 = []
		self.hit_board_2 = []
		
		self.ship_board_1 = []
		self.ship_board_2 = []
		for x in range(0,10):
			self.hit_board_1.append([])
			self.hit_board_2.append([])

			self.ship_board_1.append([])
			self.ship_board_2.append([])
			for y in range(0,10):
				self.hit_board_1[x].append(0)
				self.hit_board_2[x].append(0)

				self.ship_board_1[x].append(0)
				self.ship_board_2[x].append(0)
		####################################################### LOADERS #######################################################

		# FIXME: Nie działa dynamiczne skalowanie, dodać skalowanie ładowanek obrazka i pozycjonowanie względem domyślnej rozdzielczości
     
	def Start(self):
		
		print("############################################################")
		print("                       BATTLESHIPS                          ")
		print("                    github.com/Tymiec                       ")
		print("############################################################\n")

		self.Intro()

		while True :
			self.Menu()

	def screen_refresh(self):
		
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				exit()
			elif event.type == VIDEORESIZE:
				self.this_windows = pygame.display.set_mode((event.size[1] * self.frame_scale, event.size[1]), HWSURFACE|DOUBLEBUF|RESIZABLE)
		
		self.this_windows.blit(pygame.transform.scale(self.obraz, self.this_windows.get_rect().size),(0, 0))
		pygame.display.update()
		self.game_clock.tick(self.fps)
		

	def Intro(self):
		
		if not self.wait_or_skip(32):
			return
		
		pygame.mixer.music.load("Assets/Sound/intro.ogg")
		pygame.mixer.music.play()
		
		for i in range(0, 4):
			self.obraz.blit(self.introSprite, Rect(192, 352, 608, 320), Rect(0, i * 320, 608, 320))	
			if not self.wait_or_skip(32):
				return
		if not self.wait_or_skip(180):
			return
			
		pygame.mixer.music.stop()
	
	def Menu(self):

		self.screen_refresh()
		
		while True :
			self.Play_music()
			self.obraz.blit(self.menu_backgrund, self.menu_backgrund.get_rect())
			# BUTTONS
			# BUTTON PLAY
			if self.play_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
				self.obraz.blit(self.preparation_background, self.preparation_background.get_rect())
				self.screen_refresh()
				preparation_loop = True
				self.player_move = True
				self.computer_move = False
				while preparation_loop is True: #TODO
					self.Play_music()
					# BUTTONI
					# GAME LOOP START
					if self.generation_counter == 0:
						self.ship_board_2 = self.generate_whole_board(self.ship_board_2)
						self.generation_counter = 1
					if self.generate_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1 and self.generation_counter_2 == 0:
						# print("generate player board")
						# self.Clean_boards()
						self.generation_counter_2 = 1
						self.place_player_ship_counter = 20
						# print(self.ship_board_1)
						# self.wait_or_skip(60)
						self.ship_board_1 = self.generate_whole_board(self.ship_board_1)
						print("essa")
					if self.start_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
						game_loop = True
						self.DeleteRestricions()
						self.obraz.blit(self.preparation_background, self.preparation_background.get_rect())
						while game_loop is True: #TODO check both ship_board for 10's and change them to 0
							self.Play_music()
							if self.exit_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
								print("Thanks for playing!")
								pygame.quit()
								sys.exit()
							if self.back_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
								game_loop = False
								self.screen_refresh() 
								self.wait_or_skip(10)
								# self.Computer_targeting() #debugging for computer targeting
							self.screen_refresh()
							if self.player_move is True:
								if pygame.mouse.get_pressed()[0] == 1:
									mouse_pos_1 = pygame.mouse.get_pos()
									for x in range(0,10):
										for y in range(0,10):
											# print(mouse_pos_1)
											check_pos = Rect(x * 38 + 578, y * 38 + 258, 38, 38)
											if check_pos.collidepoint(mouse_pos_1[0], mouse_pos_1[1]) == True:
												print(f"Add hit to computer board on x: {x}| y: {y}")
												if self.ship_board_2[x][y] == 3 and self.hit_board_2[x][y] != 1 and self.hit_board_2[x][y] != 2: #sprawdzamy czy jest tam statek i czy juz nie strzelalismy
													self.hit_board_2[x][y] = 1 
													self.player_shot_counter += 1
													self.player_succesfull_hit_counter += 1
													print(f"Player succesfull hits: {self.player_succesfull_hit_counter}")
													self.player_move = True
													self.computer_move = False
												elif self.ship_board_2[x][y] == 0 and self.hit_board_2[x][y] != 1 and self.hit_board_2[x][y] != 2: #sprawdzamy czy jest tam statek i czy juz nie strzelalismy
													# print(self.ship_board_2[x][y])
													self.hit_board_2[x][y] = 2 
													self.player_shot_counter += 1
													self.player_move = False
													self.computer_move = True
												# else: #DEBUG OUTPUT
												# 	print("You can't hit this square again")
												# 	print(f"Position is x: {x}| y: {y}")
												# 	print("plansza statkow 2")
												# 	print(self.plansza_statkow_2)
												# 	print("plansza trafien 2")
												# 	print(self.plansza_trafien_2)
							for x in range(0,10):
								for y in range(0,10):
									# test_fog_of_war = random.randint(4,6)
									self.obraz.blit(self.hit_sprite, Rect(x * 38 + 66, y * 38 + 258, 38, 38), Rect(self.hit_board_1[x][y] * 38, 0, 38, 38)) 
									#TODO: dodać hit_alpha_sprite nakładany na plansze statkow gracza po strzalach komputera
									self.obraz.blit(self.hit_sprite, Rect(x * 38 + 578, y * 38 + 258, 38, 38), Rect(self.hit_board_2[x][y] * 38, 0, 38, 38))
							self.screen_refresh()
							if self.player_succesfull_hit_counter == 20 or self.computer_succesfull_hit_counter == self.place_player_ship_counter:
								end_screen_loop = True
								self.Change_number_to_array()
								# TODO: dodać animację wygranej
								self.wait_or_skip(10)
								# END SCREEN LOOP
								while end_screen_loop is True:
									self.obraz.blit(self.end_background, self.end_background.get_rect())
									if self.exit_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
										print("Thanks for playing!")
										pygame.quit()
										sys.exit()
									if self.back_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
										end_screen_loop = False
										game_loop = False
										preparation_loop = False
										self.screen_refresh() 
										self.wait_or_skip(10)
										# 34 
									
									# print(self.player_shot_counter_array)
									if self.player_shot_counter_array != []:
										for x in range(2):						 #pozycja   x             y wymiary | odejmujemy 2 od x
											self.obraz.blit(self.numbers, Rect(x * 34 + 384, 685, 34, 30), Rect(self.player_shot_counter_array[x] * 34, 0, 34, 30))
									if self.player_succesfull_hit_counter_array != []:
										for x in range(2):
											self.obraz.blit(self.numbers, Rect(x * 34 + 384, 730, 34, 30), Rect(self.player_succesfull_hit_counter_array[x] * 34, 0, 34, 30))
									if self.computer_shot_counter_array != []:
										for x in range(2):						 #pozycja   x             y wymiary | odejmujemy 2 od x
											self.obraz.blit(self.numbers, Rect(x * 34 + 894, 685, 34, 30), Rect(self.computer_shot_counter_array[x] * 34, 0, 34, 30))
									if self.computer_succesfull_hit_counter_array != []:
										for x in range(2):
											self.obraz.blit(self.numbers, Rect(x * 34 + 894, 730, 34, 30), Rect(self.computer_succesfull_hit_counter_array[x] * 34, 0, 34, 30))	
									self.screen_refresh()
								# END SCREEN LOOP
							if self.computer_move is True:
								self.computer_move = False
								self.player_move = True
								for i in range(1):
									self.Computer_targeting()
									# self.wait_or_skip(60)
								
								
					# GAME LOOP END
					if self.back_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
						self.Clean_boards()
						self.generation_counter = 0
						self.generation_counter_2 = 0
						preparation_loop = False

					if self.exit_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
						print("Thanks for playing!")
						pygame.quit()
						sys.exit()
					# BUTTONI
					# GAME PREPARATION
					for x in range(0,10):
						for y in range(0,10):
							self.obraz.blit(self.hit_sprite, Rect(x * 38 + 66, y * 38 + 258, 38, 38), Rect(self.ship_board_1[x][y] * 38, 0, 38, 38))
							self.obraz.blit(self.hit_sprite, Rect(x * 38 + 578, y * 38 + 258, 38, 38), Rect(self.ship_board_2[x][y] * 38, 0, 38, 38)) # DEBUG view of computer board
							# self.obraz.blit(self.hit_sprite, Rect(x * 38 + 578, y * 38 + 258, 38, 38), Rect(5 * 38, 0, 38, 38))

					# HIT REGISTER
					if pygame.mouse.get_pressed()[0] == 1:
						mouse_pos_1 = pygame.mouse.get_pos()
						for x in range(0,10):
							for y in range(0,10):
								# print(mouse_pos_1)
								check_pos = Rect(x * 38 + 66, y * 38 + 258, 38, 38)
								# self.obraz.blit(self.hit_sprite,Rect(x * 38 + 66, y * 38 + 258, 38, 38), Rect(5 * 38, 0, 38, 38))
								if check_pos.collidepoint(mouse_pos_1[0], mouse_pos_1[1]) == True and self.ship_board_1[x][y] != 10 and self.ship_board_1[x][y] != 3 and self.place_player_ship_counter < 20:
									# print(f"Add ship to player board on x: {x}| y: {y}")
									self.ship_board_1[x][y] = 3 # zmiana kwadratu na statek
									self.MarkAsOccupiedFromThisField(self.ship_board_1, x, y)
									self.place_player_ship_counter += 1 
									# print(f"Ships placed by player: {self.place_player_ship_counter}")
					# HIT REGISTER
					# GAME PREPARATION

					self.screen_refresh()
				# PREPARATION PHASE
			# BUTTON PLAY

			# # BUTTON OPTIONS
			if self.options_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
				self.obraz.blit(self.options, self.options.get_rect())
				options_loop = True
				# OPTIONS LOOP
				while options_loop is True:
					if self.back_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
						options_loop = False
					if self.exit_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
						print("Thanks for playing!")
						pygame.quit()
						sys.exit()
					self.screen_refresh()
				# OPTIONS LOOP
			# # BUTTON OPTIONS

        	# # BUTTON CREDITS
			if self.credits_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
				# Załadowanie BUTTONu creditsów TODO: Dodać powrót do menu
				self.obraz.blit(self.credits, self.credits.get_rect())
				self.screen_refresh()
				credits_loop = True
				while credits_loop is True:
					if pygame.mouse.get_pressed()[0] == 1:
						mouse_pos_1 = pygame.mouse.get_pos()
						# print(mouse_pos_1)
					if self.back_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
						credits_loop = False
					if self.exit_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
						# print("Thanks for playing!")
						# mouse_pos_1 = pygame.mouse.get_pos()
						# print(mouse_pos_1[0])
						# print(mouse_pos_1[1])
						pygame.quit()
						sys.exit()
					self.screen_refresh()
			# # BUTTON CREDITS

        	# # BUTTON EXIT
			if self.exit_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
				print("Thanks for playing!")
				pygame.quit()
				sys.exit()
			# # BUTTON EXIT

			self.screen_refresh()
	
	#########################
	#		FUNCTIONS 		#
	#########################

	def wait_or_skip(self, frames):
		for _ in range(0, frames):
			check_press = pygame.key.get_pressed()
			if check_press[K_RETURN]:
				return False 
			self.screen_refresh()
		return True

	def Play_music (self) :
		if not pygame.mixer.music.get_busy() :
			not_different = True
			while not_different is True:
				new_selected = random.randint(0,2)
				if self.selected_song != new_selected:
					self.selected_song = new_selected
					not_different = False
			pygame.mixer.music.load(self.music[self.selected_song])
			pygame.mixer.music.play()
			# print(f"Now playing: {self.music[self.selected_song]}")

	def Rotate(self):
		self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
		self.rect = self.image.get_rect(center=self.rect.center)

	def Update(self):
		self.angle += 10
		self.Rotate()

	def Clean_selected_board(self):
		for x in range(0,10):
			for y in range(0,10):
				self.ship_board_1[x][y] = 0

	def Clean_boards(self):
		self.hit_board_1 = []
		self.hit_board_2 = []
		self.ship_board_1 = []
		self.ship_board_2 = []
		self.place_player_ship_counter = 0
		for x in range(0,10):
			self.hit_board_1.append([])
			self.hit_board_2.append([])

			self.ship_board_1.append([])
			self.ship_board_2.append([])
			for y in range(0,10):
				self.hit_board_1[x].append(0)
				self.hit_board_2[x].append(0)

				self.ship_board_1[x].append(0)
				self.ship_board_2[x].append(0)

	def MarkAsOccupiedFromThisField(self, board, x, y):
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

	def DeleteRestricions(self):
		for x in range(0,10):
			for y in range(0,10):
				if self.ship_board_1[x][y] == 10:
					self.ship_board_1[x][y] = 0
				if self.ship_board_2[x][y] == 10:
					self.ship_board_2[x][y] = 0

	# def Generate_ai_board(self): #TODO przycisk dla graca 
	# 	# statki = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
	# 	random_x = -1
	# 	random_y = -1

	# 	for x in range(20):
	# 		not_different = True
	# 		while not_different: # random generating coordinate until we find a free spot
	# 			random_x = random.randint(0,9)
	# 			random_y = random.randint(0,9)
	# 			if self.ship_board_2[random_x][random_y] != 3 and self.ship_board_2[random_x][random_y] != 2 and self.ship_board_2[random_x][random_y] != 10:
	# 				not_different = False
	# 		if self.ship_board_2[random_x][random_y] != 3:
	# 			self.ship_board_2[random_x][random_y] = 3
	# 			self.MarkAsOccupiedFromThisField(self.ship_board_2,random_x,random_y)

	def Computer_targeting(self):
		random_x = -1
		random_y = -1

		not_different = True
		while not_different: # random generating coordinate until we find a free spot
			random_x = random.randint(0,9)
			random_y = random.randint(0,9)
			if self.hit_board_1[random_x][random_y] != 1 and self.hit_board_1[random_x][random_y] != 2 and self.hit_board_1[random_x][random_y] != 4:
				not_different = False
		# print(f"Add computer shot to: {random_x}, {random_y}") 
		if self.hit_board_1[random_x][random_y] not in [1, 2, 4, 10]: # sprawdzamy czy nie stawiamy na statku FIXME: chyba zbędny?
			if self.ship_board_1[random_x][random_y] == 3:
				self.computer_succesfull_hit_counter += 1
				# print(f"Computer succesfull hits: {self.computer_succesfull_hit_counter}")
				self.computer_shot_counter += 1
				self.hit_board_1[random_x][random_y] = 4 # mark hit
				self.MarkAsOccupiedFromThisField(self.hit_board_1, random_x, random_y)
				self.computer_move = True
				self.player_move = False
				# return True
			elif self.ship_board_1[random_x][random_y] == 0:
					self.hit_board_1[random_x][random_y] = 2 # mark miss
					self.computer_shot_counter += 1
					# return False

	def Change_number_to_array(self):
		self.player_shot_counter_array = []
		self.computer_shot_counter_array = []
		self.player_succesfull_hit_counter_array = []
		self.computer_succesfull_hit_counter_array = []

		while self.player_shot_counter != 0:
			self.player_shot_counter, d = divmod(self.player_shot_counter, 10)
			self.player_shot_counter_array.append(int(d))
			self.player_shot_counter_array.reverse()

		while self.computer_shot_counter != 0:
			self.computer_shot_counter, d = divmod(self.computer_shot_counter, 10)
			self.computer_shot_counter_array.append(int(d))
			self.computer_shot_counter_array.reverse()

		while self.player_succesfull_hit_counter != 0:
			self.player_succesfull_hit_counter, d = divmod(self.player_succesfull_hit_counter, 10)
			self.player_succesfull_hit_counter_array.append(int(d))
			self.player_succesfull_hit_counter_array.reverse()

		while self.computer_succesfull_hit_counter != 0:
			self.computer_succesfull_hit_counter, d = divmod(self.computer_succesfull_hit_counter, 10)
			self.computer_succesfull_hit_counter_array.append(int(d))
			self.computer_succesfull_hit_counter_array.reverse()

	def generate_ship(self, length, grid):
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
				self.MarkAsOccupiedFromThisField(grid, random_x, random_y + i)
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
				self.MarkAsOccupiedFromThisField(grid, random_x + i, random_y)
		
		# print(grid)
		return grid

	def generate_whole_board(self, test_grid):
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
				for x in range(0,10):
					for y in range(0,10):
						test_grid[x][y] = 0
				for i in range(len(ships_1)):
					tester = self.generate_ship(ships_1[i], test_grid)
					if tester == False: # jeżeli jakaś funkcja nie była w stanie postawić statku to zwróci False który musimy przechować przez całego for'a
						can_fit = tester # zmieniamy went_wrong z True na False żeby pętla nam się
					# print(ships_1[i])
					placement_loop = can_fit
			for x in range(0,10):
				for y in range(0,10):
					if test_grid[x][y] == 3:
						counter += 1
		return test_grid

def Main():
	battleships = Battleships()
	battleships.Start()

if __name__ == "__main__" :
	Main()