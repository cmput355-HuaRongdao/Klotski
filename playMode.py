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
def Game1():
    ver_tile_1 = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    caocao_block = Tile(red, 256, 256,128,0,"image/cao.jpeg")
    ver_tile_2 = Tile(blue, 128, 256,384,0,"image/huang_1.jpeg")
    ver_tile_3 = Tile(grey, 128, 256,0,256,"image/yun_1.jpeg")
    hor_tile_1 = Tile(dark_pink, 256, 128,128,256,"image/ma_2.jpeg")
    ver_tile_4 = Tile(grey, 128, 256,384,256,"image/Zhang_1.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,128,384,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,256,384,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_1,ver_tile_2,ver_tile_3,ver_tile_4,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,hor_tile_1,caocao_block]
    return tileList

#兵临曹营
def Game2():
    caocao_block = Tile(red, 256, 256,128,0,"image/cao.jpeg")
    ver_tile_1 = Tile(yellow, 128, 256,0,256,"image/guan_1.jpeg")
    ver_tile_2 = Tile(blue, 128, 256,384,256,"image/huang_1.jpeg")
    ver_tile_3 = Tile(grey, 128, 256,128,384,"image/yun_1.jpeg")
    ver_tile_4 = Tile(grey, 128, 256,256,384,"image/Zhang_1.jpeg")
    hor_tile_1 = Tile(dark_pink, 256, 128,128,256,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,0,128,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,128,"image/bing.jpeg")
    tileList = [ver_tile_1,ver_tile_2,ver_tile_3,ver_tile_4,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,hor_tile_1,caocao_block]
    return tileList

#五将逼宫
def Game3():
    caocao_block = Tile(red, 256, 256,128,128,"image/cao.jpeg")
    ver_tile_1 = Tile(yellow, 128, 256,0,128,"image/guan_1.jpeg")
    ver_tile_2 = Tile(blue, 128, 256,384,128,"image/huang_1.jpeg")
    hor_tile_1 = Tile(grey, 256, 128,0,0,"image/yun_2.jpeg")
    hor_tile_2 = Tile(grey, 256, 128,256,0,"image/Zhang_2.jpeg")
    hor_tile_3 = Tile(dark_pink, 256, 128,128,384,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,384,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#前呼后拥
def Game4():
    caocao_block = Tile(red, 256, 256,256,0,"image/cao.jpeg")
    hor_tile_1 = Tile(grey, 256, 128,0,128,"image/guan_2.jpeg")
    hor_tile_2 = Tile(grey, 256, 128,0,256,"image/huang_2.jpeg")
    hor_tile_3 = Tile(dark_pink, 256,128,0,384,"image/yun_2.jpeg")
    hor_tile_4 = Tile(grey, 256, 128,256,256,"image/Zhang_2.jpeg")
    hor_tile_5 = Tile(grey, 256, 128,256,384,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,128,0,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,256,512,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [hor_tile_1,hor_tile_2,hor_tile_3,hor_tile_4,hor_tile_5,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#四将连关
def Game5():
    caocao_block = Tile(red, 256, 256,0,0,"image/cao.jpeg")
    ver_tile_1 = Tile(yellow, 128, 256,0,256,"image/guan_1.jpeg")
    ver_tile_2 = Tile(blue, 128, 256,128,256,"image/huang_1.jpeg")
    hor_tile_1 = Tile(dark_pink, 256, 128,256,0,"image/yun_2.jpeg")
    hor_tile_2 = Tile(dark_pink, 256, 128,256,128,"image/Zhang_2.jpeg")
    hor_tile_3 = Tile(dark_pink, 256, 128,256,256,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,256,384,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#巧过五关
def Game6():
    caocao_block = Tile(red, 256, 256,256,0,"image/cao.jpeg")
    hor_tile_1 = Tile(grey, 256, 128,0,256,"image/guan_2.jpeg")
    hor_tile_2 = Tile(grey, 256, 128,0,384,"image/huang_2.jpeg")
    hor_tile_3 = Tile(dark_pink, 256,128,256,256,"image/yun_2.jpeg")
    hor_tile_4 = Tile(grey, 256, 128,256,384,"image/Zhang_2.jpeg")
    hor_tile_5 = Tile(grey, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,0,128,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,128,"image/bing.jpeg")
    tileList = [hor_tile_1,hor_tile_2,hor_tile_3,hor_tile_4,hor_tile_5,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#将挡后路
def Game7():
    caocao_block = Tile(red, 256, 256,0,256,"image/cao.jpeg")
    ver_tile_1 = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    ver_tile_2 = Tile(blue, 128, 256,128,0,"image/huang_1.jpeg")
    ver_tile_3 = Tile(blue, 128, 256,256,128,"image/yun_1.jpeg")
    ver_tile_4 = Tile(blue, 128, 256,384,128,"image/Zhang_1.jpeg")
    ver_tile_5 = Tile(blue, 128, 256,256,384,"image/ma_1.jpeg")
    sm_tile_1 = Tile(center, 128, 128,256,0,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    tileList = [ver_tile_1,ver_tile_2,ver_tile_3,ver_tile_4,ver_tile_5,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#四面八方
def Game8():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_1 = Tile(yellow, 128, 256,0,256,"image/guan_1.jpeg")
    ver_tile_2 = Tile(blue, 128, 256,384,256,"image/huang_1.jpeg")
    hor_tile_1 = Tile(dark_pink, 256,128,128,0,"image/yun_2.jpeg")
    hor_tile_2 = Tile(grey, 256, 128,128,128,"image/Zhang_2.jpeg")
    hor_tile_3 = Tile(grey, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,128,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,384,128,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#近在咫尺
def Game9():
    caocao_block = Tile(red, 256, 256,0,384,"image/cao.jpeg")
    ver_tile_1 = Tile(yellow, 128, 256,256,0,"image/guan_1.jpeg")
    ver_tile_2 = Tile(blue, 128, 256,384,0,"image/huang_1.jpeg")
    ver_tile_3 = Tile(blue, 128, 256,256,256,"image/yun_1.jpeg")
    ver_tile_4 = Tile(blue, 128, 256,384,256,"image/Zhang_1.jpeg")
    hor_tile_1 = Tile(dark_pink, 256, 128,0,128,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,256,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,128,256,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,256,512,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_1,ver_tile_2,ver_tile_3,ver_tile_4,hor_tile_1,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#无横之局 samw with jiangdanghoulu
def Game10():
    caocao_block = Tile(red, 256, 256,0,256,"image/cao.jpeg")
    ver_tile_1 = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    ver_tile_2 = Tile(blue, 128, 256,128,0,"image/huang_1.jpeg")
    ver_tile_3 = Tile(blue, 128, 256,256,128,"image/yun_1.jpeg")
    ver_tile_4 = Tile(blue, 128, 256,384,128,"image/Zhang_1.jpeg")
    ver_tile_5 = Tile(blue, 128, 256,256,384,"image/ma_1.jpeg")
    sm_tile_1 = Tile(center, 128, 128,256,0,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    tileList = [ver_tile_1,ver_tile_2,ver_tile_3,ver_tile_4,ver_tile_5,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#星罗棋布
def Game11():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_1 = Tile(yellow, 128, 256,0,128,"image/guan_1.jpeg")
    ver_tile_2 = Tile(blue, 128, 256,384,128,"image/huang_1.jpeg")
    hor_tile_1 = Tile(dark_pink, 256, 128,128,0,"image/yun_2.jpeg")
    hor_tile_2 = Tile(dark_pink, 256, 128,128,128,"image/Zhang_2.jpeg")
    hor_tile_3 = Tile(dark_pink, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,0,384,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#比翼横空
def Game12():
    caocao_block = Tile(red, 256, 256,256,0,"image/cao.jpeg")
    ver_tile_1 = Tile(yellow, 128, 256,384,384,"image/guan_1.jpeg")
    hor_tile_1 = Tile(grey, 256, 128,0,0,"image/huang_2.jpeg")
    hor_tile_2 = Tile(dark_pink, 256,128,0,128,"image/yun_2.jpeg")
    hor_tile_3 = Tile(grey, 256, 128,0,256,"image/Zhang_2.jpeg")
    hor_tile_4 = Tile(grey, 256, 128,256,256,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,384,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,256,384,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,256,512,"image/bing.jpeg")
    tileList = [ver_tile_1,hor_tile_1,hor_tile_2,hor_tile_3,hor_tile_4,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#牛气冲天
def Game13():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_1 = Tile(yellow, 128, 256,0,256,"image/guan_1.jpeg")
    ver_tile_2 = Tile(blue, 128, 256,384,256,"image/huang_1.jpeg")
    hor_tile_1 = Tile(dark_pink, 256, 128,0,128,"image/yun_2.jpeg")
    hor_tile_2 = Tile(dark_pink, 256, 128,256,128,"image/Zhang_2.jpeg")
    hor_tile_3 = Tile(dark_pink, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,0,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#背水列阵
def Game14():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_1 = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    ver_tile_2 = Tile(blue, 128, 256,384,0,"image/huang_1.jpeg")
    hor_tile_1 = Tile(dark_pink, 256, 128,128,0,"image/yun_2.jpeg")
    hor_tile_2 = Tile(dark_pink, 256, 128,0,512,"image/Zhang_2.jpeg")
    hor_tile_3 = Tile(dark_pink, 256, 128,256,512,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,384,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,384,384,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,128,128,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,256,128,"image/bing.jpeg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#调兵遣将
def Game15():
    caocao_block = Tile(red, 256, 256,0,0,"image/cao.jpeg")
    hor_tile_1 = Tile(grey, 256, 128,0,256,"image/guan_2.jpeg")
    hor_tile_2 = Tile(grey, 256, 128,0,384,"image/huang_2.jpeg")
    hor_tile_3 = Tile(dark_pink, 256,128,256,256,"image/yun_2.jpeg")
    hor_tile_4 = Tile(grey, 256, 128,256,384,"image/Zhang_2.jpeg")
    hor_tile_5 = Tile(grey, 256, 128,128,512,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,256,0,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,384,0,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,256,128,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,384,128,"image/bing.jpeg")
    tileList = [hor_tile_1,hor_tile_2,hor_tile_3,hor_tile_4,hor_tile_5,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#逃之夭夭
def Game16():
    caocao_block = Tile(red, 256, 256,128,256,"image/cao.jpeg")
    ver_tile_1 = Tile(yellow, 128, 256,0,0,"image/guan_1.jpeg")
    ver_tile_2 = Tile(blue, 128, 256,0,256,"image/huang_1.jpeg")
    ver_tile_3 = Tile(blue, 128, 256,384,0,"image/yun_1.jpeg")
    ver_tile_4 = Tile(blue, 128, 256,384,256,"image/Zhang_1.jpeg")
    hor_tile_1 = Tile(dark_pink, 256, 128,128,0,"image/ma_2.jpeg")
    sm_tile_1 = Tile(center, 128, 128,0,512,"image/bing.jpeg")
    sm_tile_2 = Tile(black, 128, 128,384,512,"image/bing.jpeg")
    sm_tile_3 = Tile(black, 128, 128,128,128,"image/bing.jpeg")
    sm_tile_4 = Tile(black, 128, 128,256,128,"image/bing.jpeg")
    tileList = [ver_tile_1,ver_tile_2,ver_tile_3,ver_tile_4,hor_tile_1,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList