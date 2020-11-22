import pygame
import pygame.rect
#https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite


class Tile(pygame.sprite.Sprite):
	def __init__(self, color=0, width=0, height=0,position_x = 0,position_y = 0,file = None):
		pygame.sprite.Sprite.__init__(self)
		self.width = width
		self.height = height
		self.color = color
		self.image = pygame.image.load(file)
		self.rect = self.image.get_rect()
		
		self.rect.x = position_x
		self.rect.y = position_y
		self.previous_x = 0
		self.previous_y = 0

	def check_collision(self,previous_pos,tile_group):
		collision_list = pygame.sprite.spritecollide(self, tile_group, False)
		if len(collision_list) > 1:
			self.rect.x = self.previous_x
			self.rect.y = self.previous_y
			return False
		
	def update_pos(self, new_x, new_y,current_offset_x,current_offset_y):
		self.previous_x = self.rect.x
		self.previous_y = self.rect.y
		self.rect.x = new_x
		self.rect.y = new_y

		# check for clicked position
		if current_offset_x < -100 and -100 < current_offset_y < -30:
			self.rect.x = self.previous_x + 128
		elif current_offset_x > -30 and -100 < current_offset_y < -30:
			self.rect.x = self.previous_x - 128
		elif current_offset_y < -100 and -100 < current_offset_x < -30 :
			self.rect.y = self.previous_y + 128
		elif current_offset_y > -30 and -100 < current_offset_x < -30:
			self.rect.y = self.previous_y - 128
		

		if self.rect.x + self.width >= 512:
			self.rect.x = 512 - self.width
		elif self.rect.x <= 0:
			self.rect.x = 0
		if self.rect.y + self.height >= 640:
			self.rect.y = 640 - self.height
		elif self.rect.y<=0:
			self.rect.y = 0 
		