import pygame
import pygame.rect
import sys
import playMode
from huarong import solve

pygame.init()
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(240, 128, 128)
lightPurple = pygame.Color(153, 0, 153)
# Font and window size
window_size = window_width, window_height = 1024, 864
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("Klotski")
menuFont = pygame.font.SysFont("comicsansms", 24)
text_font = pygame.font.SysFont("comicsansms", 80)
num = None
# The buttons' positions
mode_up_y = 450
mode_down_y = 500
choose_left_x = 190
choose_right_x = 390
end_left_x = 620
end_right_x = 820
end_up_y = 700
end_down_y = 750
one_unit = 64
four_unit = 256
eight_unit = 512
success_x = 128
success_y = 384

def choose_mode(mouse_x, mouse_y):
	# set up the choosen mode button
	left_x, right_x, up_y,down_y = choose_left_x, choose_right_x, mode_up_y, mode_down_y
	button_click(left_x, right_x, up_y, down_y, mouse_x, mouse_y)
	mode = menuFont.render('CHOOSE MODE', True, white)
	window.blit(mode, (202, 460))

def end_game(mouse_x, mouse_y):
	# set up the end game button
	left_x, right_x, up_y, down_y = end_left_x, end_right_x, 450, 500
	button_click(left_x, right_x, up_y, down_y, mouse_x, mouse_y)
	end = menuFont.render('END GAME', True, white)
	window.blit(end, (660, 460))

def startMenu():
	# the page with lists of games
	global num
	while True:
		window.fill(white)
		largeText = text_font
		klotski = largeText.render('WELCOME TO KLOTSKI', True, black)
		rect = klotski.get_rect()
		rect.center = (window_width / 2, window_height / 4)
		window.blit(klotski, rect)
		# get the user's mouse position
		mouse_x, mouse_y = pygame.mouse.get_pos()
		# choose and end game button
		choose_mode(mouse_x, mouse_y)
		end_game(mouse_x, mouse_y)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN: 
				# start game
				if choose_left_x < mouse_x < choose_right_x and\
				 mode_up_y < mouse_y < mode_down_y:
					mode, num = choose()
					return mode
				# end game
				elif end_left_x < mouse_x < end_right_x and\
				 mode_up_y < mouse_y < mode_down_y:
					pygame.quit() 
					sys.exit()
		pygame.display.update()

def button_click(left_x, right_x, up_y, down_y, mouse_x, mouse_y):
	# setting of clicking buttons
	# the color will be changed when user's mouse is over it 
	if left_x < mouse_x < right_x and up_y < mouse_y < down_y:
		pygame.draw.rect(window, lightPurple, (left_x, up_y, right_x - left_x, down_y - up_y))
	else:
		pygame.draw.rect(window, red, (left_x, up_y, right_x - left_x, down_y - up_y))

def choose():
	# This function is used to choose modes
	while True:
		window.fill(white)
		text = pygame.font.SysFont("comicsansms", 40)
		listLength = 16
		textList = []
		# get the playmode's name, from Game1 to Game 16
		for i in range(0, listLength):
			num = str(i + 1)
			textList.append('Game' + num)
		position = []
		for i in range(len(textList)):
			position.append((0, 50 * i))
		# choose the mode by getting position from user's mouse
		for i in range(len(textList)):
			modeName = text.render(str(i + 1) + " " + textList[i], True, black)
			rect = modeName.get_rect()
			rect.topleft = position[i]
			text_width = modeName.get_width()
			text_height = modeName.get_height()

			mouse_x, mouse_y = pygame.mouse.get_pos()
			if position[i][0] < mouse_x < position[i][0] + text_width and \
			position[i][1] < mouse_y < position[i][1] + text_height:
				modeName = text.render(str(i + 1) + " " + textList[i], True, red)
			window.blit(modeName,rect)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# mouse left click
				if event.button == 1:
					for i in range(len(textList)):
						# start game
						if position[i][1] < mouse_y < position[i][1]+40:
							method = getattr(playMode, textList[i])
							return method(), textList[i]
		pygame.display.update()
		
		
def game_over(mouse_x,mouse_y):
	# end the game fuction
	if one_unit < mouse_x < four_unit and \
	end_up_y < mouse_y < end_down_y:
		game_over = True
		return game_over

def quit_game():
	# click to quit the game
	mouse_x, mouse_y = pygame.mouse.get_pos()
	left_x, right_x, up_y, down_y = one_unit, four_unit, end_up_y, end_down_y
	button_click(left_x, right_x, up_y, down_y, mouse_x, mouse_y)
	quitGame = menuFont.render('QUIT', True, white)
	window.blit(quitGame,(90, 710))

def answer_button():
	# click to see the solution
	mouse_x, mouse_y = pygame.mouse.get_pos()
	left_x, right_x, up_y, down_y = 320, eight_unit, end_up_y, end_down_y
	button_click(left_x, right_x, up_y, down_y, mouse_x, mouse_y)
	solution_button = menuFont.render('ANSWER', True, white)
	window.blit(solution_button,(330, 710))

def success():
	# set up the sucess page
	while True:
		window.fill(white)
		text = text_font
		congratulations = text.render('Congratulations!!', True, red)
		rect = congratulations.get_rect()
		rect.center = (window_width/2, window_height/2)
		window.blit(congratulations,rect)
        # click to back to menu
		back = text.render("Back to menu", True, black)
		rect = back.get_rect()
		rect.center = (window_width/2, 2*window_height/3)
		text_width = back.get_width()
		text_height = back.get_height()
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if rect[0] < mouse_x < rect[0]+text_width and rect[1] < mouse_y < rect[1]+text_height:
			back = text.render("Back to menu", True, red)
		window.blit(back,rect)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN: 
				# start game
				if rect[0] < mouse_x < rect[0] + text_width and\
				 rect[1] < mouse_y < rect[1] + text_height:
					return True
		pygame.display.update()

def game_over_page():
	# set up the game over page
		window.fill(white)
		text = text_font
		congratulations = text.render('GAME OVER', True, red)
		rect = congratulations.get_rect()
		rect.center = (window_width / 2, window_height / 2)
		window.blit(congratulations,rect)

		back = text.render("Back to menu", True, black)
		rect = back.get_rect()
		rect.center = (window_width / 2, 2 * window_height / 3)
		text_width = back.get_width()
		text_height = back.get_height()
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if rect[0] < mouse_x < rect[0] + text_width and \
		rect[1] < mouse_y < rect[1] + text_height:
			back = text.render("Back to menu", True, red)
		window.blit(back, rect)

		pygame.display.update()

def solution(mouse_x, mouse_y):
	# connect solution file to this file so user can see the solution
	if 320 < mouse_x < eight_unit and\
	 end_up_y < mouse_y < + end_down_y:
		f = open('search_solutions/' + num + '.txt')
		solve(f)
		game_over_page()

def collision(mouse_x, mouse_y,tileList,tile_group,event):
	# This function is used to implement the collision between tiles, so make sure they can not collide to each other
	for i in tile_group:
		if mouse_x <= i.rect.x + i.width and \
			mouse_x >= i.rect.x and mouse_y <= i.rect.y + i.height and\
			mouse_y >= i.rect.y:
				current = i
				current_offset_x = i.rect.x - event.pos[0]
				current_offset_y = i.rect.y - event.pos[1]
				previous_pos = event.pos
				if current != None:
					current.update_pos(event.pos[0] + current_offset_x, event.pos[1] + \
						current_offset_y,current_offset_x,current_offset_y)
					current.check_collision(previous_pos,tile_group)
# main game 
def game(tileList,tile_group):
	clock = pygame.time.Clock()
	game_over = False
	current = None
	# current is the tile that user's clicking/dragging
	while not game_over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_over = True
			# run the collision fuction when mouse button is down
			elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_x, mouse_y = event.pos
					collision(mouse_x, mouse_y,tileList,tile_group,event)
					# quit game
					if one_unit < mouse_x < four_unit and end_up_y < mouse_y < end_down_y:
						game_over = True
						return game_over
					solution(mouse_x, mouse_y)
					
			elif event.type == pygame.MOUSEBUTTONUP:
			# the tile is not select when the mouse button is up
				current = None

			Caocao = tile_group.sprites()[9]
			# when caocao tile moves to the success position, user wins the game
			if Caocao.rect.x == success_x and Caocao.rect.y == success_y:
				return success()
	
		window.fill(white)
		# show the tiles
		tile_group.draw(window)
		
		quit_game()
		answer_button()
		
		pygame.display.update()
		clock.tick(200)

def player_main():
	while True:
		modeTiles = startMenu()
		# citation: https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Group
		# used for solving collide problem, I learnt how to use it from this website
		tile_group = pygame.sprite.Group()
		for item in modeTiles :
			tile_group.add(item)
		gameOver = game(modeTiles,tile_group)
		if gameOver == True :
			tile_group.empty()
         
if __name__ == "__main__":
	player_main()

