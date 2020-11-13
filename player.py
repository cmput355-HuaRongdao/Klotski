import pygame
import pygame.rect
import sys


blue = pygame.Color(187,255,255)
center = pygame.Color(211,211,211)
yellow = pygame.Color(230,230,250)
white = pygame.Color(255, 255, 255)
dark_pink = pygame.Color(255,182,193)
black = pygame.Color(0, 0, 0)
grey = pygame.Color(100, 100, 100)
red = pygame.Color(240,128,128)




WIDTH = 1024
HEIGHT = 864

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
		self.hspeed = 0
		self.vspeed = 0

	def check_collision(self,previous_pos):
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
		if self.rect.x>=384:
                        self.rect.x=384
                elif self.rect.x<=0:
                        self.rect.x =0
                if self.rect.y>=512:
                        self.rect.y = 512
                elif self.rect.y<=0:
                        self.rect.y = 0 

ver_tile_1 = Tile(yellow, 128, 256,0,0,"left.jpg")
caocao_block = Tile(red, 256, 256,128,0,"cube.jpg")
ver_tile_2 = Tile(blue, 128, 256,384,0,"left.jpg")
ver_tile_3 = Tile(grey, 128, 256,0,256,"left.jpg")
hor_tile_1 = Tile(dark_pink, 256, 128,128,256,"right.jpg")
ver_tile_4 = Tile(grey, 128, 256,384,256,"left.jpg")
sm_tile_1 = Tile(center, 128, 128,0,512,"cube copy.jpg")
sm_tile_2 = Tile(black, 128, 128,128,384,"cube copy.jpg")
sm_tile_3 = Tile(black, 128, 128,256,384,"cube copy.jpg")
sm_tile_4 = Tile(black, 128, 128,384,512,"cube copy.jpg")
tile_group = pygame.sprite.Group()
tile_group.add(ver_tile_1)
tile_group.add(ver_tile_2)
tile_group.add(ver_tile_3)
tile_group.add(ver_tile_4)
tile_group.add(sm_tile_1)
tile_group.add(sm_tile_2)
tile_group.add(sm_tile_3)
tile_group.add(sm_tile_4)
tile_group.add(hor_tile_1)
tile_group.add(caocao_block)


def display_rect(tile):
	pygame.draw.rect(window, tile.color, (tile.rect.x, tile.rect.y, tile.width, tile.height))
    



pygame.init()
window_size = window_width, window_height = 1024, 864
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("Klotski")

game_over = False
current = None
clock = pygame.time.Clock()
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = event.pos
				for i in tile_group:
					if mouse_x<=i.rect.x+i.width and \
						mouse_x>=i.rect.x and mouse_y<=i.rect.y+i.height and\
							mouse_y>=i.rect.y :
							current = i
							current_offset_x = i.rect.x - event.pos[0]
							current_offset_y = i.rect.y - event.pos[1]
		elif event.type == pygame.MOUSEBUTTONUP:
			current = None
		elif event.type == pygame.MOUSEMOTION:
			previous_pos = event.pos
			if current != None:
				print(current_offset_x)
				current.update_pos(event.pos[0]+current_offset_x, event.pos[1]+current_offset_y,current_offset_x,current_offset_y)
				current.check_collision(previous_pos)
			
			
					              
      
	window.fill(white)
	display_rect(ver_tile_1)
	display_rect(caocao_block)
	display_rect(ver_tile_2)
	display_rect(ver_tile_3)
	display_rect(ver_tile_4)
	display_rect(hor_tile_1)
	display_rect(sm_tile_1)
	display_rect(sm_tile_2)
	display_rect(sm_tile_3)
	display_rect(sm_tile_4)
	pygame.display.update()
	clock.tick(200)

pygame.quit()
sys.exit()
