import pygame ,sys

WINDOW_HEIGHT = 675
WINDOW_WIDTH = 1200


class Button():
	def __init__(self, pos_x,pos_y,scale, img):
		width = img.get_width()
		height = img.get_height()
		self.image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (pos_x, pos_y)
		self.pos_unhover = (pos_x, pos_y)
		self.pos_hover = (pos_x, pos_y + 3)
	
	def draw(self, screen):
		screen.blit(self.image, self.rect)
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			self.rect.center = self.pos_hover
		else:
			self.rect.center = self.pos_unhover


class Button_Horse():
	def __init__(self, pos_x, pos_y, scale, img):
		width = img.get_width()
		height = img.get_height()
		self.image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (pos_x, pos_y)
		self.pos_unhover = (pos_x, pos_y)
		self.pos_hover = (pos_x, pos_y + 10)
		self.click = False
	def draw(self, screen):
		screen.blit(self.image, self.rect)
		pos = pygame.mouse.get_pos()
		if self.rect.collidepoint(pos):
			self.rect.center = self.pos_hover
		else:
			self.rect.center = self.pos_unhover
		
		if self.click:
			pygame.draw.circle(screen, (52, 235, 79) , self.rect.center, 60, 3)
    
