import pygame
import pygame.rect
import sys
SHADOW = pygame.Color(192, 192, 192)
pink = pygame.Color(255,228,225)
blue = pygame.Color(187,255,255)
center = pygame.Color(211,211,211)
yellow = pygame.Color(230,230,250)
white = pygame.Color(255, 255, 255)
dark_pink = pygame.Color(255,182,193)
black = pygame.Color(0, 0, 0)
grey = pygame.Color(100, 100, 100)
silver = pygame.Color(200, 200, 200)
red = pygame.Color(240,128,128)
green = pygame.Color(0, 255, 0)


#https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite
class Tile(pygame.sprite.Sprite):
	def __init__(self, color=0, width=0, height=0,position_x = 0,position_y = 0):
		pygame.sprite.Sprite.__init__(self)
		self.width = width
		self.height = height
		self.color = color
		self.position_x = position_x
		self.position_y = position_y

ver_tile_1 = Tile(yellow, 128, 256,0,0)
caocao_block = Tile(red, 256, 256,128,0)
ver_tile_2 = Tile(blue, 128, 256,384,0)
ver_tile_3 = Tile(grey, 128, 256,0,256)
hor_tile_1 = Tile(dark_pink, 256, 128,128,256)
ver_tile_4 = Tile(grey, 128, 256,384,256)
sm_tile_1 = Tile(center, 128, 128,0,512)
sm_tile_2 = Tile(black, 128, 128,128,384)
sm_tile_3 = Tile(black, 128, 128,256,384)
sm_tile_4 = Tile(black, 128, 128,384,512)

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


def display_rect(block):
	pygame.draw.rect(window, block.color, (block.position_x, block.position_y, block.width, block.height))
    
pygame.init()
window_size = window_width, window_height = 1024, 864
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
m_down = False
m_up = False
stop_drag = False
game_over = False
current = None
clock = pygame.time.Clock()
while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				mouse_x, mouse_y = event.pos
				for i in tile_group:
					if mouse_x<=i.position_x+i.width and \
						mouse_x>=i.position_x and mouse_y<=i.position_y+i.height and\
							mouse_y>=i.position_y:
							current = i
							offset_x = i.position_x - event.pos[0]
							offset_y = i.position_y - event.pos[1]
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == 1:
				current = None
		elif event.type == pygame.MOUSEMOTION:
			if current != None:
				current.position_x = event.pos[0]+offset_x
				current.position_y = event.pos[1]+offset_y
			
					              
      
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
	clock.tick(25)

pygame.quit()
sys.exit()
