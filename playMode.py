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
def Hengdaolima():
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
    tileList = [ver_tile_1,ver_tile_2,ver_tile_3,ver_tile_4,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,hor_tile_1,caocao_block]
    return tileList

#兵临曹营
def Binglincaoying():
    caocao_block = Tile(red, 256, 256,128,0,"cube.jpg")
    ver_tile_1 = Tile(yellow, 128, 256,0,256,"left.jpg")
    ver_tile_2 = Tile(blue, 128, 256,384,256,"left.jpg")
    ver_tile_3 = Tile(grey, 128, 256,128,384,"left.jpg")
    ver_tile_4 = Tile(grey, 128, 256,256,384,"left.jpg")
    hor_tile_1 = Tile(dark_pink, 256, 128,128,256,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,0,0,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,0,128,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,384,0,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,384,128,"cube copy.jpg")
    tileList = [ver_tile_1,ver_tile_2,ver_tile_3,ver_tile_4,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,hor_tile_1,caocao_block]
    return tileList

#五将逼宫
def Wujiangbigong():
    caocao_block = Tile(red, 256, 256,128,128,"cube.jpg")
    ver_tile_1 = Tile(yellow, 128, 256,0,128,"left.jpg")
    ver_tile_2 = Tile(blue, 128, 256,384,128,"left.jpg")
    hor_tile_1 = Tile(grey, 256, 128,0,0,"right.jpg")
    hor_tile_2 = Tile(grey, 256, 128,256,0,"right.jpg")
    hor_tile_3 = Tile(dark_pink, 256, 128,128,384,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,0,384,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,0,512,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,384,384,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,384,512,"cube copy.jpg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#前呼后拥
def Qianhuhouyong():
    caocao_block = Tile(red, 256, 256,256,0,"cube.jpg")
    hor_tile_1 = Tile(grey, 256, 128,0,128,"right.jpg")
    hor_tile_2 = Tile(grey, 256, 128,0,256,"right.jpg")
    hor_tile_3 = Tile(dark_pink, 256,128,0,384,"right.jpg")
    hor_tile_4 = Tile(grey, 256, 128,256,256,"right.jpg")
    hor_tile_5 = Tile(grey, 256, 128,256,384,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,0,0,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,128,0,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,256,512,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,384,512,"cube copy.jpg")
    tileList = [hor_tile_1,hor_tile_2,hor_tile_3,hor_tile_4,hor_tile_5,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#四将连关
def Sijianglianguan():
    caocao_block = Tile(red, 256, 256,0,0,"cube.jpg")
    ver_tile_1 = Tile(yellow, 128, 256,0,256,"left.jpg")
    ver_tile_2 = Tile(blue, 128, 256,128,256,"left.jpg")
    hor_tile_1 = Tile(dark_pink, 256, 128,256,0,"right.jpg")
    hor_tile_2 = Tile(dark_pink, 256, 128,256,128,"right.jpg")
    hor_tile_3 = Tile(dark_pink, 256, 128,256,256,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,0,512,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,384,512,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,256,384,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,384,384,"cube copy.jpg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#巧过五关
def Qiaoguowuguan():
    caocao_block = Tile(red, 256, 256,128,0,"cube.jpg")
    hor_tile_1 = Tile(dark_pink, 256, 128,0,256,"right.jpg")
    hor_tile_2 = Tile(dark_pink, 256, 128,0,384,"right.jpg")
    hor_tile_3 = Tile(dark_pink, 256, 128,256,256,"right.jpg")
    hor_tile_4 = Tile(dark_pink, 256, 128,256,384,"right.jpg")
    hor_tile_5 = Tile(dark_pink, 256, 128,128,512,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,0,0,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,0,128,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,384,0,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,384,128,"cube copy.jpg")
    tileList = [hor_tile_1,hor_tile_2,hor_tile_3,hor_tile_4,hor_tile_5,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#将挡后路
def Jiangdanghoulu():
    caocao_block = Tile(red, 256, 256,0,256,"cube.jpg")
    ver_tile_1 = Tile(yellow, 128, 256,0,0,"left.jpg")
    ver_tile_2 = Tile(blue, 128, 256,128,0,"left.jpg")
    ver_tile_3 = Tile(blue, 128, 256,256,128,"left.jpg")
    ver_tile_4 = Tile(blue, 128, 256,384,128,"left.jpg")
    ver_tile_5 = Tile(blue, 128, 256,256,384,"left.jpg")
    sm_tile_1 = Tile(center, 128, 128,256,0,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,384,0,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,0,512,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,384,384,"cube copy.jpg")
    tileList = [ver_tile_1,ver_tile_2,ver_tile_3,ver_tile_4,ver_tile_5,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#四面八方
def Simianbafang():
    caocao_block = Tile(red, 256, 256,128,256,"cube.jpg")
    ver_tile_1 = Tile(yellow, 128, 256,0,256,"left.jpg")
    ver_tile_2 = Tile(blue, 128, 256,384,256,"left.jpg")
    hor_tile_1 = Tile(dark_pink, 256, 128,128,0,"right.jpg")
    hor_tile_2 = Tile(dark_pink, 256, 128,128,128,"right.jpg")
    hor_tile_3 = Tile(dark_pink, 256, 128,128,512,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,0,128,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,384,128,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,0,512,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,384,512,"cube copy.jpg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#近在咫尺
def Jinzaizhichi():
    caocao_block = Tile(red, 256, 256,0,384,"cube.jpg")
    ver_tile_1 = Tile(yellow, 128, 256,256,0,"left.jpg")
    ver_tile_2 = Tile(blue, 128, 256,384,0,"left.jpg")
    ver_tile_3 = Tile(blue, 128, 256,256,256,"left.jpg")
    ver_tile_4 = Tile(blue, 128, 256,384,256,"left.jpg")
    hor_tile_1 = Tile(dark_pink, 256, 128,0,128,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,0,256,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,128,256,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,256,512,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,384,512,"cube copy.jpg")
    tileList = [ver_tile_1,ver_tile_2,ver_tile_3,ver_tile_4,hor_tile_1,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#无横之局 samw with jiangdanghoulu
def Wuhengzhiju():
    caocao_block = Tile(red, 256, 256,0,256,"cube.jpg")
    ver_tile_1 = Tile(yellow, 128, 256,0,0,"left.jpg")
    ver_tile_2 = Tile(blue, 128, 256,128,0,"left.jpg")
    hor_tile_1 = Tile(dark_pink, 256, 128,128,0,"right.jpg")
    hor_tile_2 = Tile(dark_pink, 256, 128,128,128,"right.jpg")
    hor_tile_3 = Tile(dark_pink, 256, 128,128,512,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,256,0,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,384,0,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,0,512,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,384,384,"cube copy.jpg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#星罗棋布
def Xingluoqibu():
    caocao_block = Tile(red, 256, 256,128,256,"cube.jpg")
    ver_tile_1 = Tile(yellow, 128, 256,0,128,"left.jpg")
    ver_tile_2 = Tile(blue, 128, 256,384,128,"left.jpg")
    hor_tile_1 = Tile(dark_pink, 256, 128,128,0,"right.jpg")
    hor_tile_2 = Tile(dark_pink, 256, 128,128,128,"right.jpg")
    hor_tile_3 = Tile(dark_pink, 256, 128,128,512,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,0,0,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,384,0,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,0,384,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,384,384,"cube copy.jpg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#比翼横空
def Biyihengkong():
    caocao_block = Tile(red, 256, 256,256,0,"cube.jpg")
    ver_tile_1 = Tile(dark_pink, 128, 256,384,384,"left.jpg")
    hor_tile_1 = Tile(blue, 256, 128,0,0,"right.jpg")
    hor_tile_2 = Tile(dark_pink, 256, 128,0,128,"right.jpg")
    hor_tile_3 = Tile(grey, 256, 128,0,256,"right.jpg")
    hor_tile_4 = Tile(yellow, 256, 128,256,256,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,0,384,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,0,512,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,256,384,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,256,512,"cube copy.jpg")
    tileList = [ver_tile_1,hor_tile_1,hor_tile_2,hor_tile_3,hor_tile_4,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#牛气冲天
def Niuqichongtian():
    caocao_block = Tile(red, 256, 256,128,256,"cube.jpg")
    ver_tile_1 = Tile(yellow, 128, 256,0,256,"left.jpg")
    ver_tile_2 = Tile(blue, 128, 256,384,256,"left.jpg")
    hor_tile_1 = Tile(dark_pink, 256, 128,0,128,"right.jpg")
    hor_tile_2 = Tile(dark_pink, 256, 128,256,128,"right.jpg")
    hor_tile_3 = Tile(dark_pink, 256, 128,128,512,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,0,0,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,384,0,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,0,512,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,384,512,"cube copy.jpg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#背水列阵
def Beishuiliuzhen():
    caocao_block = Tile(red, 256, 256,128,256,"cube.jpg")
    ver_tile_1 = Tile(yellow, 128, 256,0,0,"left.jpg")
    ver_tile_2 = Tile(blue, 128, 256,384,0,"left.jpg")
    hor_tile_1 = Tile(dark_pink, 256, 128,128,0,"right.jpg")
    hor_tile_2 = Tile(dark_pink, 256, 128,0,512,"right.jpg")
    hor_tile_3 = Tile(dark_pink, 256, 128,256,512,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,0,384,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,384,384,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,128,128,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,256,128,"cube copy.jpg")
    tileList = [ver_tile_1,ver_tile_2,hor_tile_1,hor_tile_2,hor_tile_3,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#调兵遣将
def Diaobingqianjiang():
    caocao_block = Tile(red, 256, 256,0,0,"cube.jpg")
    hor_tile_1 = Tile(dark_pink, 256, 128,0,256,"right.jpg")
    hor_tile_2 = Tile(blue, 256, 128,0,384,"right.jpg")
    hor_tile_3 = Tile(dark_pink, 256, 128,256,256,"right.jpg")
    hor_tile_4 = Tile(yellow, 256, 128,256,384,"right.jpg")
    hor_tile_5 = Tile(grey, 256, 128,128,512,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,256,0,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,384,0,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,256,128,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,384,128,"cube copy.jpg")
    tileList = [hor_tile_1,hor_tile_2,hor_tile_3,hor_tile_4,hor_tile_5,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList

#逃之夭夭
def Taozhiyaoyao():
    caocao_block = Tile(red, 256, 256,128,256,"cube.jpg")
    ver_tile_1 = Tile(yellow, 128, 256,0,0,"left.jpg")
    ver_tile_2 = Tile(blue, 128, 256,0,256,"left.jpg")
    ver_tile_3 = Tile(blue, 128, 256,384,0,"left.jpg")
    ver_tile_4 = Tile(blue, 128, 256,384,256,"left.jpg")
    hor_tile_1 = Tile(dark_pink, 256, 128,128,0,"right.jpg")
    sm_tile_1 = Tile(center, 128, 128,0,512,"cube copy.jpg")
    sm_tile_2 = Tile(black, 128, 128,384,512,"cube copy.jpg")
    sm_tile_3 = Tile(black, 128, 128,128,128,"cube copy.jpg")
    sm_tile_4 = Tile(black, 128, 128,256,128,"cube copy.jpg")
    tileList = [ver_tile_1,ver_tile_2,ver_tile_3,ver_tile_4,hor_tile_1,sm_tile_1,sm_tile_2,sm_tile_3,sm_tile_4,caocao_block]
    return tileList