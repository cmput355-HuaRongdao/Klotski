import pygame
import pygame.rect
import sys
import playMode
#from huarong import solve

pygame.init()
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
red = pygame.Color(240,128,128)
lightPurple = pygame.Color(153,0,153)

def display_rect(tile):
	pygame.draw.rect(window, tile.color, (tile.rect.x, tile.rect.y, tile.width, tile.height))

window_size = window_width, window_height = 1024, 864
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
pygame.display.set_caption("Klotski")
menuFont = pygame.font.SysFont("comicsansms",24)
num = None

def startMenu():
	global num
	while True:
		window.fill(white)
		largeText = pygame.font.SysFont("comicsansms",80)
		klotski = largeText.render('WELCOME TO KLOTSKI', True, black)
		rect = klotski.get_rect()
		rect.center = (window_width/2, window_height/4)
		window.blit(klotski,rect)
		
		# mouse position index
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if 190 < mouse_x < 190+200 and 450 < mouse_y < 450+50:
			pygame.draw.rect(window, lightPurple, (190, 450, 200, 50))
		else:
			pygame.draw.rect(window, red, (190, 450, 200, 50))

		if 620 < mouse_x < 620+200 and 450 < mouse_y < 450+50:
			pygame.draw.rect(window, lightPurple, (620, 450, 200, 50))
		else:
			pygame.draw.rect(window, red, (620, 450, 200, 50))

		# set button text
		mode = menuFont.render('CHOOSE MODE', True, white)
		end = menuFont.render('END GAME', True, white)
		window.blit(mode,(202, 460))
		window.blit(end,(660, 460))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit
			elif event.type == pygame.MOUSEBUTTONDOWN: 
				# start game
				if 200 < mouse_x < 200+200 and 450 < mouse_y < 450+50:
					mode, num = choose()
					return mode
				# end game
				elif 650 < mouse_x < 650+200 and 450 < mouse_y < 450+50:
					pygame.quit() 
					sys.exit()
		pygame.display.update()



def choose():
	while True:
		window.fill(white)
		text = pygame.font.SysFont("comicsansms",40)
		listLength = 16
		textList = []
		for i in range(0,listLength):
			num = str(i+1)
			textList.append('Game'+num)
		position = []
		for i in range(len(textList)):
			position.append((0,50*i))

		for i in range(len(textList)):
			modeName = text.render(str(i+1)+" "+textList[i], True, black)
			rect = modeName.get_rect()
			rect.topleft = position[i]
			text_width = modeName.get_width()
			text_height = modeName.get_height()
			# mouse position index
			mouse_x, mouse_y = pygame.mouse.get_pos()
			if position[i][0] < mouse_x < position[i][0]+text_width and position[i][1] < mouse_y < position[i][1]+text_height:
				modeName = text.render(str(i+1)+" "+textList[i], True, red)
			window.blit(modeName,rect)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit
			elif event.type == pygame.MOUSEBUTTONDOWN: 
				for i in range(len(textList)):
					# start game
					if position[i][1] < mouse_y < position[i][1]+40:
						method = getattr(playMode, textList[i])
						return method(),textList[i]
		pygame.display.update()
		
		

def success():
	while True:
		window.fill(white)
		largeText = pygame.font.SysFont("comicsansms",80)
		congratulations = largeText.render('Congratulations!!', True, red)
		rect = congratulations.get_rect()
		rect.center = (window_width/2, window_height/2)
		window.blit(congratulations,rect)

		text = pygame.font.SysFont("comicsansms",80)
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
				sys.exit
			elif event.type == pygame.MOUSEBUTTONDOWN: 
				# start game
				if rect[0] < mouse_x < rect[0]+text_width and rect[1] < mouse_y < rect[1]+text_height:
					return True
		pygame.display.update()
# def solution_button():

# main game 
def game(tileList,tile_group):
	clock = pygame.time.Clock()
	game_over = False
	current = None
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
								previous_pos = event.pos
								if current != None:
									current.update_pos(event.pos[0]+current_offset_x, event.pos[1]+current_offset_y,current_offset_x,current_offset_y)
									current.check_collision(previous_pos,tile_group)
					
					# quit game
					if 64 < mouse_x < 256 and 700 < mouse_y < 700+50:
						game_over = True
						return game_over
					'''if 320 < mouse_x < 512 and 700 < mouse_y <700+50:
						f = open('search_solutions/'+num+'.txt')
						solve(f)
						return game_over'''

			elif event.type == pygame.MOUSEBUTTONUP:
				current = None

			Caocao = tile_group.sprites()[9]
			if Caocao.rect.x == 128 and Caocao.rect.y == 384:
				return success()
	
		window.fill(white)
		for item in tileList :
			display_rect(item)
		
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if 64 < mouse_x <256 and 700 < mouse_y < 700+50:
			pygame.draw.rect(window, lightPurple, (64, 700, 128, 50))
		else:
			pygame.draw.rect(window, red, (64, 700, 128, 50))
		if 320 < mouse_x < 512 and 700 < mouse_y <700+50:
			pygame.draw.rect(window, lightPurple, (320, 700, 128, 50))
		else:
			pygame.draw.rect(window, red, (320, 700, 128, 50))

		# set button text
		quitGame = menuFont.render('QUIT', True, white)
		solution_button = menuFont.render('ANSWER', True, white)
		window.blit(quitGame,(90, 710))
		window.blit(solution_button,(330, 710))
		pygame.display.update()
		clock.tick(200)

def main():
	while True:
		modeTiles = startMenu()
		tile_group = pygame.sprite.Group()
		for item in modeTiles :
			tile_group.add(item)
		gameOver = game(modeTiles,tile_group)
		if gameOver == True :
			tile_group.empty()




if __name__ == "__main__":
	main()

