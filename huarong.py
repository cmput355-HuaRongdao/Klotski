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


# create our windows


def draw_border(screen):
    pygame.draw.rect(screen, black, (LEFT_b, UP_b, 10, five_units))
    pygame.draw.rect(screen, black, (LEFT_b, UP_b, four_units, 10))
    pygame.draw.rect(screen, black, (RIGHT_b, UP_b, 10, five_units))
    pygame.draw.rect(screen, black, (LEFT_b, DOWN_b, UNIT, 10))
    pygame.draw.rect(screen, black, (right_short_arm_start, DOWN_b, unit_plt, 10))


# This function is our first method to display our solution of the game, we use coloured rectangular to represent
# different chesses. Caocao was represent by white, Huangzhong to yellow, Machao to silver, Zhaoyun to grey,
# Guanyu to red, Bing to blue, Zhangfei to green.
# file f comes from search_solution.

def solve_no_picture(f):
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
    display_list = temp_list.strip("[")
    display_list = display_list.strip("]")
    display_list = display_list.split(",")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Klotski")
    list_index = 0
    for row in range(5):
        for column in range(1,5):
            current_ch = display_list[list_index][column]
        list_index = list_index + 1
    list_index = 0

    draw_border(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if list_index < len(display_list):
            for x in range(5):
                for y in range(1, 5):
                    current_ch = display_list[list_index][y]
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


# Same logic of solve_no_picture, but added pictures. Pictures come from http://www.4399.com/flash/2546_1.htm.

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
    display_list = temp_list.strip("[")
    display_list = display_list.strip("]")
    display_list = display_list.split(",")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Klotski")
    list_index = 0
    for row in range(5):
        for column in range(1,5):
            current_ch = display_list[list_index][column]
        list_index = list_index + 1
    list_index = 0

    color = black

    check_huang = 0
    check_cao = 0
    check_ma = 0
    check_yun = 0
    check_guan = 0
    check_zhang = 0

    # convert the images to a proper size.

    img_huang1 = pygame.image.load("image/huang_1.PNG")
    img_huang1 = pygame.transform.scale(img_huang1, (int(UNIT), int(2*UNIT)))
    img_huang2 = pygame.image.load("image/huang_2.PNG")
    img_huang2 = pygame.transform.scale(img_huang2, (int(2*UNIT), int(UNIT)))

    img_ma1 = pygame.image.load("image/ma_1.PNG")
    img_ma1 = pygame.transform.scale(img_ma1, (int(UNIT), int(2*UNIT)))
    img_ma2 = pygame.image.load("image/ma_2.PNG")
    img_ma2 = pygame.transform.scale(img_ma2, (int(2*UNIT), int(UNIT)))

    img_yun1 = pygame.image.load("image/yun_1.PNG")
    img_yun1 = pygame.transform.scale(img_yun1, (int(UNIT), int(2*UNIT)))
    img_yun2= pygame.image.load("image/yun_2.PNG")
    img_yun2 = pygame.transform.scale(img_yun2, (int(2*UNIT), int(UNIT)))

    img_guan1 = pygame.image.load("image/guan_1.PNG")
    img_guan1 = pygame.transform.scale(img_guan1, (int(UNIT), int(2*UNIT)))
    img_guan2= pygame.image.load("image/guan_2.PNG")
    img_guan2 = pygame.transform.scale(img_guan2, (int(2*UNIT), int(UNIT)))

    img_zhang1 = pygame.image.load("image/zhang_1.PNG")
    img_zhang1 = pygame.transform.scale(img_zhang1, (int(UNIT), int(2*UNIT)))
    img_zhang2 = pygame.image.load("image/zhang_2.PNG")
    img_zhang2 = pygame.transform.scale(img_zhang2, (int(2*UNIT), int(UNIT)))

    img_cao = pygame.image.load("image/cao.PNG")
    img_cao = pygame.transform.scale(img_cao, (int(2*UNIT), int(2*UNIT)))

    img_bing = pygame.image.load("image/bing.PNG")
    img_bing = pygame.transform.scale(img_bing, (int(UNIT), int(UNIT)))

    draw_border(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if list_index < len(display_list):
            for x in range(5):
                for y in range(1, 5):
                    current_ch = display_list[list_index][y]

                    # add graph
                    try:
                        if current_ch == "h" and check_huang == 0 and display_list[list_index][y+1] == "h":
                            screen.blit(img_huang2, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                            check_huang = 1
                        elif current_ch == "h" and check_huang != 0:
                            continue
                        elif current_ch == "h" and check_huang == 0 and display_list[list_index][y+1] != "h":
                            screen.blit(img_huang1, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                            check_huang = 1
                        elif current_ch == "$" and check_cao == 0 :
                            screen.blit(img_cao, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                            check_cao = 1
                        elif current_ch == "$" and check_cao != 0:
                            continue
                        elif current_ch == "m" and check_ma == 0 and display_list[list_index][y+1] == "m":
                            screen.blit(img_ma2, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                            check_ma = 1
                        elif current_ch == "m" and check_ma != 0:
                            continue
                        elif current_ch == "m" and check_ma == 0 and display_list[list_index][y+1] != "m":
                            screen.blit(img_ma1, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                            check_ma = 1
                        elif current_ch == "y" and check_yun == 0 and display_list[list_index][y+1] == "y":
                            screen.blit(img_yun2, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                            check_yun = 1
                        elif current_ch == "y" and check_yun != 0:
                            continue
                        elif current_ch == "y" and check_yun == 0 and display_list[list_index][y+1] != "y":
                            screen.blit(img_yun1, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                            check_yun = 1
                        elif current_ch == "g" and check_guan == 0 and display_list[list_index][y+1] == "g":
                            screen.blit(img_guan2, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                            check_guan = 1
                        elif current_ch == "g" and check_guan != 0:
                            continue
                        elif current_ch == "g" and check_guan == 0 and display_list[list_index][y+1] != "g":
                            screen.blit(img_guan1, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                            check_guan = 1
                        elif current_ch == "z" and check_zhang == 0 and display_list[list_index][y+1] == "z":
                            screen.blit(img_zhang2, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                            check_zhang = 1
                        elif current_ch == "z" and check_zhang != 0:
                            continue
                        elif current_ch == "z" and check_zhang == 0 and display_list[list_index][y+1] != "z":
                            screen.blit(img_zhang1, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                            check_zhang = 1
                        elif current_ch == "@" :
                            screen.blit(img_bing, (LEFT_b + UNIT * (y-1), UP_b + UNIT * x , UNIT, UNIT))
                        elif current_ch == "." :
                            pygame.draw.rect(screen, black, (LEFT_b + UNIT * (y - 1), UP_b + UNIT * x, UNIT, UNIT))
                    except:
                        continue

                list_index = list_index + 1
            check_huang = 0
            check_cao = 0
            check_ma = 0
            check_yun = 0
            check_guan = 0
            check_zhang = 0
            pygame.display.update()
        else:
            break
        pygame.time.delay(300)
        pygame.display.update()
# if __name__ == '__main__':
#     main()
#     sys.exit()