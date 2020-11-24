from Tile import Tile
import pygame

blue = pygame.Color(187,255,255)
center = pygame.Color(211,211,211)
yellow = pygame.Color(230,230,250)
white = pygame.Color(255, 255, 255)
dark_pink = pygame.Color(255,182,193)
black = pygame.Color(0, 0, 0)
grey = pygame.Color(100, 100, 100)
red = pygame.Color(240,128,128)
lightPurple = pygame.Color(153,0,153)

#横刀立马
def game_1():
    ver_tile_one = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    caocao_block = Tile(red, 256, 256,128,0,"image/cao.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,0,"image/huang_1.jpeg")
    ver_tile_three = Tile(grey, 128, 256,0,256,"image/yun_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,128,256,"image/ma_2.jpeg")
    ver_tile_four = Tile(grey, 128, 256,384,256,"image/Zhang_1.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,128,384,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,256,384,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,ver_tile_three,ver_tile_four,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,hor_tile_one,caocao_block]
    return tileList

#兵临曹营
def game_2():
    caocao_block = Tile(red, 256, 256,128,0,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,256,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,256,"image/huang_1.jpeg")
    ver_tile_three = Tile(grey, 128, 256,128,384,"image/yun_1.jpeg")
    ver_tile_four = Tile(grey, 128, 256,256,384,"image/Zhang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,128,256,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,0,128,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,128,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,ver_tile_three,ver_tile_four,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,hor_tile_one,caocao_block]
    return tileList

#五将逼宫
def game_3():
    caocao_block = Tile(red, 256, 256,128,128,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,128,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,128,"image/huang_1.jpeg")
    hor_tile_one = Tile(grey, 256, 128,0,0,"image/yun_2.jpeg")
    hor_tile_two = Tile(grey, 256, 128,256,0,"image/Zhang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256, 128,128,384,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,384,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,hor_tile_one,hor_tile_two,hor_tile_three,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#前呼后拥
def game_4():
    caocao_block = Tile(red, 256, 256,256,0,"image/cao.jpeg")
    hor_tile_one = Tile(grey, 256, 128,0,128,"image/guan_2.jpeg")
    hor_tile_two = Tile(grey, 256, 128,0,256,"image/huang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256,128,0,384,"image/yun_2.jpeg")
    hor_tile_four = Tile(grey, 256, 128,256,256,"image/Zhang_2.jpeg")
    hor_tile_five = Tile(grey, 256, 128,256,384,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,128,0,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,256,512,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [hor_tile_one,hor_tile_two,hor_tile_three,hor_tile_four,hor_tile_five,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#四将连关
def game_5():
    caocao_block = Tile(red, 256, 256,0,0,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,256,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,128,256,"image/huang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,256,0,"image/yun_2.jpeg")
    hor_tile_two = Tile(dark_pink, 256, 128,256,128,"image/Zhang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256, 128,256,256,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,256,384,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,hor_tile_one,hor_tile_two,hor_tile_three,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#巧过五关
def game_6():
    caocao_block = Tile(red, 256, 256,128,0,"image/cao.jpeg")
    hor_tile_one = Tile(grey, 256, 128,0,256,"image/guan_2.jpeg")
    hor_tile_two = Tile(grey, 256, 128,0,384,"image/huang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256,128,256,256,"image/yun_2.jpeg")
    hor_tile_four = Tile(grey, 256, 128,256,384,"image/Zhang_2.jpeg")
    hor_tile_five = Tile(grey, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,0,128,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,128,"image/bing.jpeg")
    tileList = [hor_tile_one,hor_tile_two,hor_tile_three,hor_tile_four,hor_tile_five,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#将挡后路
def game_7():
    caocao_block = Tile(red, 256, 256,0,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,128,0,"image/huang_1.jpeg")
    ver_tile_three = Tile(blue, 128, 256,256,128,"image/yun_1.jpeg")
    ver_tile_four = Tile(blue, 128, 256,384,128,"image/Zhang_1.jpeg")
    ver_tile_five = Tile(blue, 128, 256,256,384,"image/ma_1.jpeg")
    sm_tile_one = Tile(center, 128, 128,256,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,ver_tile_three,ver_tile_four,ver_tile_five,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#四面八方
def game_8():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,256,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,256,"image/huang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256,128,128,0,"image/yun_2.jpeg")
    hor_tile_two = Tile(grey, 256, 128,128,128,"image/Zhang_2.jpeg")
    hor_tile_three = Tile(grey, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,128,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,128,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,hor_tile_one,hor_tile_two,hor_tile_three,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#近在咫尺
def game_9():
    caocao_block = Tile(red, 256, 256,0,384,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,256,0,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,0,"image/huang_1.jpeg")
    ver_tile_three = Tile(blue, 128, 256,256,256,"image/yun_1.jpeg")
    ver_tile_four = Tile(blue, 128, 256,384,256,"image/Zhang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,0,128,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,256,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,128,256,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,256,512,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,ver_tile_three,ver_tile_four,hor_tile_one,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#无横之局 samw with jiangdanghoulu
def game_10():
    caocao_block = Tile(red, 256, 256,0,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,128,0,"image/huang_1.jpeg")
    ver_tile_three = Tile(blue, 128, 256,256,128,"image/yun_1.jpeg")
    ver_tile_four = Tile(blue, 128, 256,384,128,"image/Zhang_1.jpeg")
    ver_tile_five = Tile(blue, 128, 256,256,384,"image/ma_1.jpeg")
    sm_tile_one = Tile(center, 128, 128,256,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,ver_tile_three,ver_tile_four,ver_tile_five,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#星罗棋布
def game_11():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,128,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,128,"image/huang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,128,0,"image/yun_2.jpeg")
    hor_tile_two = Tile(dark_pink, 256, 128,128,128,"image/Zhang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,0,384,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,hor_tile_one,hor_tile_two,hor_tile_three,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#比翼横空
def game_13():
    caocao_block = Tile(red, 256, 256,256,0,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,384,384,"image/guan_1.jpeg")
    hor_tile_one = Tile(grey, 256, 128,0,0,"image/huang_2.jpeg")
    hor_tile_two = Tile(dark_pink, 256,128,0,128,"image/yun_2.jpeg")
    hor_tile_three = Tile(grey, 256, 128,0,256,"image/Zhang_2.jpeg")
    hor_tile_four = Tile(grey, 256, 128,256,256,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,384,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,256,384,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,256,512,"image/bing.jpeg")
    tileList = [ver_tile_one,hor_tile_one,hor_tile_two,hor_tile_three,hor_tile_four,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#牛气冲天
def game_14():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,256,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,256,"image/huang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,0,128,"image/yun_2.jpeg")
    hor_tile_two = Tile(dark_pink, 256, 128,256,128,"image/Zhang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,hor_tile_one,hor_tile_two,hor_tile_three,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#背水列阵
def game_14():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,0,"image/huang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,128,0,"image/yun_2.jpeg")
    hor_tile_two = Tile(dark_pink, 256, 128,0,512,"image/Zhang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256, 128,256,512,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,384,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,128,128,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,256,128,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,hor_tile_one,hor_tile_two,hor_tile_three,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#调兵遣将
def game_15():
    caocao_block = Tile(red, 256, 256,0,0,"image/cao.jpeg")
    hor_tile_one = Tile(grey, 256, 128,0,256,"image/guan_2.jpeg")
    hor_tile_two = Tile(grey, 256, 128,0,384,"image/huang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256,128,256,256,"image/yun_2.jpeg")
    hor_tile_four = Tile(grey, 256, 128,256,384,"image/Zhang_2.jpeg")
    hor_tile_five = Tile(grey, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,256,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,256,128,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,128,"image/bing.jpeg")
    tileList = [hor_tile_one,hor_tile_two,hor_tile_three,hor_tile_four,hor_tile_five,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#逃之夭夭
def game_16():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,0,256,"image/huang_1.jpeg")
    ver_tile_three = Tile(blue, 128, 256,384,0,"image/yun_1.jpeg")
    ver_tile_four = Tile(blue, 128, 256,384,256,"image/Zhang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,128,0,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,128,128,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,256,128,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,ver_tile_three,ver_tile_four,hor_tile_one,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList