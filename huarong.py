import pygame
import sys

# display resolution:
WIDTH = 1024
HEIGHT = 864

# border scales:
UNIT = WIDTH/8
LEFT_b = WIDTH/12
RIGHT_b = LEFT_b + 4*UNIT
UP_b = HEIGHT/12
DOWN_b = UP_b + 5*UNIT
# bonuses:
unit_plt = UNIT + 10
right_short_arm_start = LEFT_b + 3*UNIT
two_units = 2*UNIT
three_units = 3*UNIT
four_units = 4*UNIT
five_units = 5*UNIT

# character scales:


# colors:
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BORDER_c = (255, 128, 0)

def draw_border(screen):
	pygame.draw.rect(screen, BORDER_c, (LEFT_b, UP_b, 10, five_units))
	pygame.draw.rect(screen, BORDER_c, (LEFT_b, UP_b, four_units, 10))
	pygame.draw.rect(screen, BORDER_c, (RIGHT_b, UP_b, 10, five_units))
	pygame.draw.rect(screen, BORDER_c, (LEFT_b, DOWN_b, UNIT, 10))
	pygame.draw.rect(screen, BORDER_c, (right_short_arm_start, DOWN_b, unit_plt, 10))

def draw_characters(screen):
	pygame.draw.rect(screen, RED, (LEFT_b + UNIT, UP_b, two_units, two_units))	# cao cao
	pygame.draw.rect(screen, GREEN, (LEFT_b, UP_b, UNIT, two_units))	# zhang fei
	pygame.draw.rect(screen, GREEN, (LEFT_b + three_units, UP_b, UNIT, two_units))	# zhao yun
	pygame.draw.rect(screen, GREEN, (LEFT_b, UP_b + two_units, UNIT, two_units))	# ma chao
	pygame.draw.rect(screen, GREEN, (LEFT_b + UNIT, UP_b + two_units, two_units, UNIT))	# guan yu
	pygame.draw.rect(screen, GREEN, (LEFT_b + three_units, UP_b + two_units, UNIT, two_units))	# huang zhong
	pygame.draw.rect(screen, BLUE, (LEFT_b, UP_b + four_units, UNIT, UNIT))	# bin
	pygame.draw.rect(screen, BLUE, (LEFT_b + UNIT, UP_b + three_units, UNIT, UNIT))	# bin
	pygame.draw.rect(screen, BLUE, (LEFT_b + two_units, UP_b + three_units, UNIT, UNIT))	# bin
	pygame.draw.rect(screen, BLUE, (LEFT_b + three_units, UP_b + four_units, UNIT, UNIT))	# bin

def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	game_over = False
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
		draw_border(screen)
		draw_characters(screen)
		pygame.display.update()

if __name__ == '__main__':
	main()
	sys.exit()