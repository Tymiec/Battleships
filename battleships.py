import random
import pygame
import time #TODO: usunąć jak nie będą potrzebne sleepy do sprawdzania klatek
from pygame.locals import *
from random import randrange
import pygame, sys
from pygame.locals import *
import button

class Battleships():
	
	def __init__(self):

		self.fps = 60
		frame_height = 224
		self.frame_scale = 1.142857142857143
		
		# KORDYNATY ZEROWE LEWEGO GÓRNEGO ROGU PLANSZY_1
		# X: 66 Y: 258 każde przesunięcie o x: 38 i y: 38
		# KORDYNATY ZEROWE LEWEGO GÓRNEGO ROGU PLANSZY_2
		# X: 578 Y: 258 każde przesunięcie o x: 38 i y: 38

		pygame.init()

		current_screen = pygame.display.Info()
		i = 1

		while frame_height * i < current_screen.current_h * 0.8 :
			i += 1

		pygame.mixer.init()

		self.game_clock = pygame.time.Clock()
		self.this_windows = pygame.display.set_mode((int(frame_height * i * self.frame_scale), frame_height * i), HWSURFACE|DOUBLEBUF|RESIZABLE)

		pygame.display.set_caption("BATTLESHIPS")

		self.obraz = pygame.surface.Surface(self.this_windows.get_rect().size)
		self.obraz.fill((0, 0, 0))

		####################################################### LOADERS #######################################################
		# INTRO LOADER
		self.introSprite = pygame.image.load("Assets/Grafika/intro sprite.png")

		# MENU LOADER
		self.tłoMenu = pygame.image.load("Assets/Grafika/menu.png")
		self.tloPrzygotowan = pygame.image.load("Assets/Grafika/preparation_screen.png")
		self.credits = pygame.image.load("Assets/Grafika/credits.png")

		# OPTIONS LOADER
		self.options = pygame.image.load("Assets/Grafika/options.png")

		# BUTTON LOADER
		self.play_no_hover = pygame.image.load("Assets/Grafika/play_no_hover.png").convert_alpha()
		self.play_hover = pygame.image.load("Assets/Grafika/play_hover.png").convert_alpha()
		self.play_button = button.Button(398, 385, self.play_no_hover, self.play_hover, 1)

		self.start_no_hover = pygame.image.load("Assets/Grafika/start_no_hover.png").convert_alpha()
		self.start_hover = pygame.image.load("Assets/Grafika/start_hover.png").convert_alpha()
		self.start_button = button.Button(369, 680, self.start_no_hover, self.start_hover, 1)

		self.options_no_hover = pygame.image.load("Assets/Grafika/options_no_hover.png").convert_alpha()
		self.options_hover = pygame.image.load("Assets/Grafika/options_hover.png").convert_alpha()
		self.options_button = button.Button(319, 485, self.options_no_hover, self.options_hover, 1)

		self.credits_no_hover = pygame.image.load("Assets/Grafika/credits_no_hover.png").convert_alpha()
		self.credits_hover = pygame.image.load("Assets/Grafika/credits_hover.png").convert_alpha()
		self.credits_button = button.Button(319, 635, self.credits_no_hover, self.credits_hover, 1)

		self.exit_no_hover = pygame.image.load("Assets/Grafika/exit_no_hover.png").convert_alpha()
		self.exit_hover = pygame.image.load("Assets/Grafika/exit_hover.png").convert_alpha()
		self.exit_button = button.Button(408, 735, self.exit_no_hover, self.exit_hover, 1)

		self.x_back_button = 20 #TODO: change placement of back button and possibly size?
		self.y_back_button = 20
		self.back_no_hover = pygame.image.load("Assets/Grafika/back_no_hover.png").convert_alpha()
		self.back_hover = pygame.image.load("Assets/Grafika/back_hover.png").convert_alpha()
		self.back_button = button.Button(self.x_back_button, self.y_back_button, self.back_no_hover, self.back_hover, 0.4)

		# GAME LOADERS
		self.hit_sprite = pygame.image.load("Assets/Grafika/hit_sprite.png").convert_alpha()
		# self.hit_sprite_rotate = pygame.transform.rotozoom(self.hit_sprite, 45, 1)
		self.aim = pygame.image.load('C:/Repo/Battleshipz/Assets/Grafika/aim.png').convert_alpha()

		self.place_player_ship_counter = 0

		self.plansza_trafien_1 = []
		self.plansza_trafien_2 = []
		
		self.plansza_statkow_1 = []
		self.plansza_statkow_2 = []
		for x in range(0,10):
			self.plansza_trafien_1.append([])
			self.plansza_trafien_2.append([])

			self.plansza_statkow_1.append([])
			self.plansza_statkow_2.append([])
			for y in range(0,10):
				self.plansza_trafien_1[x].append(0) # FIXME: Change to 0
				self.plansza_trafien_2[x].append(0) # FIXME: Change to 0

				self.plansza_statkow_1[x].append(0) # FIXME: Change to 0
				self.plansza_statkow_2[x].append(0) # FIXME: Change to 0
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
		
		if not self.wait_or_skip(32): #TODO: dodać napis: PRESS ENTER TO SKIP
			return
		
		pygame.mixer.music.load("Assets/Dzwiek/intro.ogg")
		pygame.mixer.music.play()
		
		for i in range(0, 4):
			self.obraz.blit(self.introSprite, Rect(192, 352, 608, 320), Rect(0, i * 320, 608, 320))	
			if not self.wait_or_skip(32):
				return
		if not self.wait_or_skip(180):
			return
			
		pygame.mixer.music.stop()
	
	def Menu(self):

		# pygame.mixer.music.load("Assets/Dzwiek/drunken_sailor_8_bit.ogg") # TODO:przyciszyć o 50%
		# pygame.mixer.music.play(-1)
		
		self.screen_refresh()
		
		while True :
			self.obraz.blit(self.tłoMenu, self.tłoMenu.get_rect())
			# PRZYCISKI

			# PRZYCISK GRAJ
			if self.play_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
				self.obraz.blit(self.tloPrzygotowan, self.tloPrzygotowan.get_rect())
				## KORDYNATY ZEROWE LEWEGO GÓRNEGO ROGU PLANSZY
				# X: 66 Y: 258 każde przesunięcie o x: 38 i y: 38
				# KORDYNATY ZEROWE LEWEGO GÓRNEGO ROGU PLANSZY
				# X: 578 Y: 258 każde przesunięcie o x: 38 i y: 38

				self.screen_refresh()
				#FIXME: potencjalny problem, jak włączymy grę i wrócimy to czy zostawić ustawienie gracza ale wyzerować ustawienie AI?
				preparation_loop = True 
				while preparation_loop is True:
					# PRZYCISKI
					# GAME LOOP
					if self.start_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
						game_loop = True
						while game_loop is True:
							print("essa")
					# GAME LOOP
					if self.back_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
						self.clean_boards()
						preparation_loop = False

					if self.exit_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
						print("Thanks for playing!")
						pygame.quit()
						sys.exit()
					# PRZYCISKI
					# GAME PREPARATION #TODO: add play button
					for x in range(0,10):
						for y in range(0,10):
							# test_fog_of_war = random.randint(4,6)
							self.obraz.blit(self.hit_sprite, Rect(x * 38 + 66, y * 38 + 258, 38, 38), Rect(self.plansza_statkow_1[x][y] * 38, 0, 38, 38))
							self.obraz.blit(self.hit_sprite, Rect(x * 38 + 578, y * 38 + 258, 38, 38), Rect(self.plansza_statkow_2[x][y] * 38, 0, 38, 38)) # TODO:add fog of war
					# HIT REGISTER
					if pygame.mouse.get_pressed()[0] == 1:
						mouse_pos_1 = pygame.mouse.get_pos()
						for x in range(0,10):
							for y in range(0,10):
								# print(mouse_pos_1)
								check_pos = Rect(x * 38 + 66, y * 38 + 258, 38, 38)
								if check_pos.collidepoint(mouse_pos_1[0], mouse_pos_1[1]) == True and self.plansza_statkow_1[x][y] != 3 and self.place_player_ship_counter < 20:
									print(f"Add ship to player board on x: {x}| y: {y}")
									self.plansza_statkow_1[x][y] = 3 # zmiana kwadratu na statek
									self.place_player_ship_counter += 1 
									print(f"Ships placed by player: {self.place_player_ship_counter}")
					# HIT REGISTER
					# GAME PREPARATION
					self.screen_refresh()
				# PREPARATION PHASE
			# PRZYCISK GRAJ

			# # PRZYCISK OPTIONS
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
			# # PRZYCISK OPTIONS

        	# # PRZYCISK CREDITS
			if self.credits_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
				# Załadowanie przycisku creditsów TODO: Dodać powrót do menu
				self.obraz.blit(self.credits, self.credits.get_rect())
				self.screen_refresh()
				credits_loop = True
				while credits_loop is True:
					if pygame.mouse.get_pressed()[0] == 1:
						mouse_pos_1 = pygame.mouse.get_pos()
						print(mouse_pos_1)
					if self.back_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
						credits_loop = False
					if self.exit_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
						print("Thanks for playing!")
						# mouse_pos_1 = pygame.mouse.get_pos()
						# print(mouse_pos_1[0])
						# print(mouse_pos_1[1])
						pygame.quit()
						sys.exit()
					self.screen_refresh()
			# # PRZYCISK CREDITS

        	# # PRZYCISK EXIT
			if self.exit_button.draw(self.obraz) and pygame.mouse.get_pressed()[0] == 1:
				print("Thanks for playing!")
				pygame.quit()
				sys.exit()
			# # PRZYCISK EXIT

			self.screen_refresh()
	
	#########################
	#		FUNKCJE  		#
	#########################

	def wait_or_skip(self, frames):
		for _ in range(0, frames):
			check_press = pygame.key.get_pressed()
			if check_press[K_RETURN]:
				return False 
				
			self.screen_refresh()
		
		return True

	def populateStatus():
		status = []
		status.append([])
		for x in range (0,4):
			for y in range (0,4):
				status[x].append(0)
		print(status)

	def rotate(self):
		self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
		self.rect = self.image.get_rect(center=self.rect.center)

	def update(self):
		self.angle += 10
		self.rotate()

	def clean_boards(self):
		self.plansza_trafien_1 = []
		self.plansza_trafien_2 = []
		self.plansza_statkow_1 = []
		self.plansza_statkow_2 = []
		self.place_player_ship_counter = 0
		for x in range(0,10):
			self.plansza_trafien_1.append([])
			self.plansza_trafien_2.append([])

			self.plansza_statkow_1.append([])
			self.plansza_statkow_2.append([])
			for y in range(0,10):
				self.plansza_trafien_1[x].append(0)
				self.plansza_trafien_2[x].append(0)

				self.plansza_statkow_1[x].append(0)
				self.plansza_statkow_2[x].append(0)

	def generate_ai_board(self):
		# statki = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
		random_x = -1
		random_y = -1

		for x in range(20):
			not_different = True
			while not_different: # random generating coordinate until we find a free spot
				random_x = random.randint(0,9)
				random_y = random.randint(0,9)
				if self.plansza_statkow_2[random_x][random_y] != 3 and self.plansza_statkow_2[random_x][random_y] != 2:
					not_different = False
			if self.plansza_statkow_2[random_x][random_y] != 3: # sprawdzamy czy nie stawiamy na statku FIXME: chyba zbędny?
				self.plansza_statkow_2[random_x][random_y] = 3 #dodajemy statek		
				# print(f"pepega {x}")
				# print(f"Generating computer ship no {x+1}")
				# for i in statki[x]:
				# 	print("EZ")
				# 	print(self.plansza_statkow_2)



def Main():
	battleships = Battleships()
	battleships.Start()

if __name__ == "__main__" :
	Main()
