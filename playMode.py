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

def Game1():
    ver_tile_one = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    caocao_block = Tile(red, 256, 256,128,0,"image/cao.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,0,"image/huang_1.jpeg")
    ver_tile_three = Tile(grey, 128, 256,0,256,"image/yun_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,128,256,"image/ma_2.jpeg")
    ver_tile_four = Tile(grey, 128, 256,384,256,"image/zhang_1.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,128,384,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,256,384,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,ver_tile_three,ver_tile_four,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,hor_tile_one,caocao_block]
    return tileList

def Game2():
    caocao_block = Tile(red, 256, 256,128,0,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,256,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,256,"image/huang_1.jpeg")
    ver_tile_three = Tile(grey, 128, 256,128,384,"image/yun_1.jpeg")
    ver_tile_four = Tile(grey, 128, 256,256,384,"image/zhang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,128,256,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,0,128,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,128,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,ver_tile_three,ver_tile_four,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,hor_tile_one,caocao_block]
    return tileList

def Game3():
    caocao_block = Tile(red, 256, 256,128,128,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,128,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,128,"image/huang_1.jpeg")
    hor_tile_one = Tile(grey, 256, 128,0,0,"image/yun_2.jpeg")
    hor_tile_two = Tile(grey, 256, 128,256,0,"image/zhang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256, 128,128,384,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,384,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,hor_tile_one,hor_tile_two,hor_tile_three,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

def Game4():
    caocao_block = Tile(red, 256, 256,256,0,"image/cao.jpeg")
    hor_tile_one = Tile(grey, 256, 128,0,128,"image/guan_2.jpeg")
    hor_tile_two = Tile(grey, 256, 128,0,256,"image/huang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256,128,0,384,"image/yun_2.jpeg")
    hor_tile_four = Tile(grey, 256, 128,256,256,"image/zhang_2.jpeg")
    hor_tile_five = Tile(grey, 256, 128,256,384,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,128,0,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,256,512,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [hor_tile_one,hor_tile_two,hor_tile_three,hor_tile_four,hor_tile_five,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

def Game5():
    caocao_block = Tile(red, 256, 256,0,0,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,256,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,128,256,"image/huang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,256,0,"image/yun_2.jpeg")
    hor_tile_two = Tile(dark_pink, 256, 128,256,128,"image/zhang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256, 128,256,256,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,256,384,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,hor_tile_one,hor_tile_two,hor_tile_three,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList


def Game6():
    caocao_block = Tile(red, 256, 256,128,0,"image/cao.jpeg")
    hor_tile_one = Tile(grey, 256, 128,0,256,"image/guan_2.jpeg")
    hor_tile_two = Tile(grey, 256, 128,0,384,"image/huang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256,128,256,256,"image/yun_2.jpeg")
    hor_tile_four = Tile(grey, 256, 128,256,384,"image/zhang_2.jpeg")
    hor_tile_five = Tile(grey, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,0,128,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,128,"image/bing.jpeg")
    tileList = [hor_tile_one,hor_tile_two,hor_tile_three,hor_tile_four,hor_tile_five,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

def Game7():
    caocao_block = Tile(red, 256, 256,0,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,128,0,"image/huang_1.jpeg")
    ver_tile_three = Tile(blue, 128, 256,256,128,"image/yun_1.jpeg")
    ver_tile_four = Tile(blue, 128, 256,384,128,"image/zhang_1.jpeg")
    ver_tile_five = Tile(blue, 128, 256,256,384,"image/ma_1.jpeg")
    sm_tile_one = Tile(center, 128, 128,256,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,ver_tile_three,ver_tile_four,ver_tile_five,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

def Game8():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,256,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,256,"image/huang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256,128,128,0,"image/yun_2.jpeg")
    hor_tile_two = Tile(grey, 256, 128,128,128,"image/zhang_2.jpeg")
    hor_tile_three = Tile(grey, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,128,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,128,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,hor_tile_one,hor_tile_two,hor_tile_three,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

def Game9():
    caocao_block = Tile(red, 256, 256,0,384,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,256,0,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,0,"image/huang_1.jpeg")
    ver_tile_three = Tile(blue, 128, 256,256,256,"image/yun_1.jpeg")
    ver_tile_four = Tile(blue, 128, 256,384,256,"image/zhang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,0,128,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,256,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,128,256,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,256,512,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,ver_tile_three,ver_tile_four,hor_tile_one,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

def Game10():
    caocao_block = Tile(red, 256, 256,0,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,128,0,"image/huang_1.jpeg")
    ver_tile_three = Tile(blue, 128, 256,256,128,"image/yun_1.jpeg")
    ver_tile_four = Tile(blue, 128, 256,384,128,"image/zhang_1.jpeg")
    ver_tile_five = Tile(blue, 128, 256,256,384,"image/ma_1.jpeg")
    sm_tile_one = Tile(center, 128, 128,256,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,ver_tile_three,ver_tile_four,ver_tile_five,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

#星罗棋布
def Game11():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,128,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,128,"image/huang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,128,0,"image/yun_2.jpeg")
    hor_tile_two = Tile(dark_pink, 256, 128,128,128,"image/zhang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,0,384,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,hor_tile_one,hor_tile_two,hor_tile_three,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

def Game12():
    caocao_block = Tile(red, 256, 256,256,0,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,384,384,"image/guan_1.jpeg")
    hor_tile_one = Tile(grey, 256, 128,0,0,"image/huang_2.jpeg")
    hor_tile_two = Tile(dark_pink, 256,128,0,128,"image/yun_2.jpeg")
    hor_tile_three = Tile(grey, 256, 128,0,256,"image/zhang_2.jpeg")
    hor_tile_four = Tile(grey, 256, 128,256,256,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,384,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,256,384,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,256,512,"image/bing.jpeg")
    tileList = [ver_tile_one,hor_tile_one,hor_tile_two,hor_tile_three,hor_tile_four,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

def Game13():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,256,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,256,"image/huang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,0,128,"image/yun_2.jpeg")
    hor_tile_two = Tile(dark_pink, 256, 128,256,128,"image/zhang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,hor_tile_one,hor_tile_two,hor_tile_three,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

def Game14():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,384,0,"image/huang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,128,0,"image/yun_2.jpeg")
    hor_tile_two = Tile(dark_pink, 256, 128,0,512,"image/zhang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256, 128,256,512,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,384,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,128,128,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,256,128,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,hor_tile_one,hor_tile_two,hor_tile_three,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

def Game15():
    caocao_block = Tile(red, 256, 256,0,0,"image/cao.jpeg")
    hor_tile_one = Tile(grey, 256, 128,0,256,"image/guan_2.jpeg")
    hor_tile_two = Tile(grey, 256, 128,0,384,"image/huang_2.jpeg")
    hor_tile_three = Tile(dark_pink, 256,128,256,256,"image/yun_2.jpeg")
    hor_tile_four = Tile(grey, 256, 128,256,384,"image/zhang_2.jpeg")
    hor_tile_five = Tile(grey, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,256,0,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,256,128,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,384,128,"image/bing.jpeg")
    tileList = [hor_tile_one,hor_tile_two,hor_tile_three,hor_tile_four,hor_tile_five,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList

def Game16():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_one = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    ver_tile_two = Tile(blue, 128, 256,0,256,"image/huang_1.jpeg")
    ver_tile_three = Tile(blue, 128, 256,384,0,"image/yun_1.jpeg")
    ver_tile_four = Tile(blue, 128, 256,384,256,"image/zhang_1.jpeg")
    hor_tile_one = Tile(dark_pink, 256, 128,128,0,"image/ma_2.jpeg")
    sm_tile_one = Tile(center, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_two = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    sm_tile_three = Tile(black, 128, 128,128,128,"image/bing.jpeg")
    sm_tile_four = Tile(black, 128, 128,256,128,"image/bing.jpeg")
    tileList = [ver_tile_one,ver_tile_two,ver_tile_three,ver_tile_four,hor_tile_one,sm_tile_one,sm_tile_two,sm_tile_three,sm_tile_four,caocao_block]
    return tileList