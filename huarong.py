import pygame
import sys
import pygame.freetype

# display resolution:
WIDTH = 1024
HEIGHT = 864

# border scales:
UNIT = WIDTH / 8
LEFT_b = WIDTH / 12
RIGHT_b = LEFT_b + 4 * UNIT
UP_b = HEIGHT / 12
DOWN_b = UP_b + 5 * UNIT

# bonuses:
unit_plt = UNIT + 10
right_short_arm_start = LEFT_b + 3 * UNIT
two_units = 2 * UNIT
three_units = 3 * UNIT
four_units = 4 * UNIT
five_units = 5 * UNIT

# colors:
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)
grey = pygame.Color(100, 100, 100)
silver = pygame.Color(200, 200, 200)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255, 255, 0)


def draw_border(screen):
    pygame.draw.rect(screen, black, (LEFT_b, UP_b, 10, five_units))
    pygame.draw.rect(screen, black, (LEFT_b, UP_b, four_units, 10))
    pygame.draw.rect(screen, black, (RIGHT_b, UP_b, 10, five_units))
    pygame.draw.rect(screen, black, (LEFT_b, DOWN_b, UNIT, 10))
    pygame.draw.rect(screen, black, (right_short_arm_start, DOWN_b, unit_plt, 10))


def draw_characters(screen):
    pygame.draw.rect(screen, red, (LEFT_b + UNIT, UP_b, two_units, two_units))  # cao cao
    pygame.draw.rect(screen, green, (LEFT_b, UP_b, UNIT, two_units))  # zhang fei
    pygame.draw.rect(screen, white, (LEFT_b + three_units, UP_b, UNIT, two_units))  # zhao yun
    pygame.draw.rect(screen, grey, (LEFT_b, UP_b + two_units, UNIT, two_units))  # ma chao
    pygame.draw.rect(screen, silver, (LEFT_b + UNIT, UP_b + two_units, two_units, UNIT))  # guan yu
    pygame.draw.rect(screen, yellow, (LEFT_b + three_units, UP_b + two_units, UNIT, two_units))  # huang zhong
    pygame.draw.rect(screen, blue, (LEFT_b, UP_b + four_units, UNIT, UNIT))  # bin
    pygame.draw.rect(screen, blue, (LEFT_b + UNIT, UP_b + three_units, UNIT, UNIT))  # bin
    pygame.draw.rect(screen, blue, (LEFT_b + two_units, UP_b + three_units, UNIT, UNIT))  # bin
    pygame.draw.rect(screen, blue, (LEFT_b + three_units, UP_b + four_units, UNIT, UNIT))  # bin


def solve(f):
    pygame.init()
    lines = f.readlines()
    temp_list = []
    row_num = 0
    for line in lines:
        if row_num > 11 or (row_num > 2 and row_num < 8) and row_num:
            line = line.replace("\n" or "[" or ']', "")
            if line != '':
                temp_list.append(line)
        row_num += 1
    temp_list = str(temp_list)
    temp_list = temp_list.replace(" " or "\n", "")
    displaylist = temp_list.strip("[")
    displaylist = displaylist.strip("]")
    displaylist = displaylist.split(",")
    print(displaylist)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Klotski")
    list_index = 0
    for row in range(5):
        for column in range(1,5):
            current_ch = displaylist[list_index][column]
            print  (current_ch)
        list_index = list_index + 1
    list_index = 0
    color = black

    draw_border(screen)
    draw_characters(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if list_index <= len(displaylist):
            for x in range(5):
                for y in range(1, 5):
                    current_ch = displaylist[list_index][y]
                    if current_ch == "h": color = yellow
                    elif current_ch == "$": color = white
                    elif current_ch == "m": color = silver
                    elif current_ch == "y": color = grey
                    elif current_ch == "g": color = red
                    elif current_ch == "@": color = blue
                    elif current_ch == "z": color = green
                    else: color = black
                    pygame.draw.rect(screen, color, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                list_index = list_index + 1
        else:
            sys.exit()
        pygame.time.delay(300)
        pygame.display.update()


# if __name__ == '__main__':
#     main()
#     sys.exit()