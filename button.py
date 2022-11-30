import pygame

class Button():
	def __init__(self, x, y, image1, image2, scale):
		# image1
		width = image1.get_width()
		height = image1.get_height()
		self.image1 = pygame.transform.scale(image1, (int(width * scale), int(height * scale)))
		self.rect = self.image1.get_rect()

		# image2
		width2 = image2.get_width()
		height2 = image2.get_height()
		self.image2 = pygame.transform.scale(image2, (int(width2 * scale), int(height2 * scale)))
		self.rect = self.image2.get_rect()

		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		pos = pygame.mouse.get_pos()
		
		if self.rect.collidepoint(pos):
			# if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
			self.clicked = True
			action = True
			surface.blit(self.image2, (self.rect.x, self.rect.y))
		else:
			surface.blit(self.image1, (self.rect.x, self.rect.y))
		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False
		return action