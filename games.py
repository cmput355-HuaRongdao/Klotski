# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
from util import *

# 逃之夭夭:
def TZYY():
	# caoCao:
	caoCao = CaoCao([1, 2])
	# Jiangs:
	zhaoYun = Jiang([3, 0], VER, 'y')
	guanYu = Jiang([1, 0], HOR, 'g')
	maChao = Jiang([0, 2], VER, 'm')
	huangZhong = Jiang([3, 2], VER, 'h')
	zhangFei = Jiang([0, 0], VER, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([1, 1])
	b2 = Bing([2, 1])
	b3 = Bing([0, 4])
	b4 = Bing([3, 4])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 无横之局:
def WHZJ():
	# caoCao:
	caoCao = CaoCao([0, 2])
	# Jiangs:
	zhaoYun = Jiang([2, 1], VER, 'y')
	guanYu = Jiang([2, 3], VER, 'g')
	maChao = Jiang([1, 0], VER, 'm')
	huangZhong = Jiang([0, 0], VER, 'h')
	zhangFei = Jiang([3, 1], VER, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([2, 0])
	b2 = Bing([3, 0])
	b3 = Bing([0, 4])
	b4 = Bing([3, 3])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 将当后路:
def JDHL():
	# caoCao:
	caoCao = CaoCao([2, 0])
	# Jiangs:
	zhaoYun = Jiang([0, 2], HOR, 'y')
	guanYu = Jiang([0, 0], HOR, 'g')
	maChao = Jiang([0, 3], HOR, 'm')
	huangZhong = Jiang([2, 2], HOR, 'h')
	zhangFei = Jiang([0, 1], HOR, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([0, 4])
	b2 = Bing([1, 4])
	b3 = Bing([2, 3])
	b4 = Bing([3, 3])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 前呼后拥:
def QHHY():
	# caoCao:
	caoCao = CaoCao([2, 0])
	# Jiangs:
	zhaoYun = Jiang([2, 2], HOR, 'y')
	guanYu = Jiang([0, 1], HOR, 'g')
	maChao = Jiang([0, 3], HOR, 'm')
	huangZhong = Jiang([2, 3], HOR, 'h')
	zhangFei = Jiang([0, 2], HOR, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([0, 0])
	b2 = Bing([1, 0])
	b3 = Bing([2, 4])
	b4 = Bing([3, 4])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 比翼横空:
def BYHK():
	# caoCao:
	caoCao = CaoCao([2, 0])
	# Jiangs:
	zhaoYun = Jiang([0, 2], HOR, 'y')
	guanYu = Jiang([0, 0], HOR, 'g')
	maChao = Jiang([2, 2], HOR, 'm')
	huangZhong = Jiang([3, 3], VER, 'h')
	zhangFei = Jiang([0, 1], HOR, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([0, 3])
	b2 = Bing([0, 4])
	b3 = Bing([2, 3])
	b4 = Bing([2, 4])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 巧过五关:
def QGWG():
	# caoCao:
	caoCao = CaoCao([1, 0])
	# Jiangs:
	zhaoYun = Jiang([0, 3], HOR, 'y')
	guanYu = Jiang([0, 2], HOR, 'g')
	maChao = Jiang([2, 3], HOR, 'm')
	huangZhong = Jiang([1, 4], HOR, 'h')
	zhangFei = Jiang([2, 2], HOR, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([0, 0])
	b2 = Bing([0, 1])
	b3 = Bing([3, 0])
	b4 = Bing([3, 1])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 五将逼宫:
def WJBG():
	# caoCao:
	caoCao = CaoCao([1, 1])
	# Jiangs:
	zhaoYun = Jiang([1, 3], HOR, 'y')
	guanYu = Jiang([0, 0], HOR, 'g')
	maChao = Jiang([0, 1], VER, 'm')
	huangZhong = Jiang([3, 1], VER, 'h')
	zhangFei = Jiang([2, 0], HOR, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([0, 3])
	b2 = Bing([0, 4])
	b3 = Bing([3, 3])
	b4 = Bing([3, 4])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 兵临曹营:
def BLCY():
	# caoCao:
	caoCao = CaoCao([1, 0])
	# Jiangs:
	zhaoYun = Jiang([3, 2], VER, 'y')
	guanYu = Jiang([1, 2], HOR, 'g')
	maChao = Jiang([1, 3], VER, 'm')
	huangZhong = Jiang([2, 3], VER, 'h')
	zhangFei = Jiang([0, 2], VER, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([0, 0])
	b2 = Bing([0, 1])
	b3 = Bing([3, 0])
	b4 = Bing([3, 1])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 四将连关:
def SJLG():
	# caoCao:
	caoCao = CaoCao([0, 0])
	# Jiangs:
	zhaoYun = Jiang([2, 2], HOR, 'y')
	guanYu = Jiang([2, 0], HOR, 'g')
	maChao = Jiang([0, 2], VER, 'm')
	huangZhong = Jiang([1, 2], VER, 'h')
	zhangFei = Jiang([2, 1], HOR, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([0, 4])
	b2 = Bing([2, 3])
	b3 = Bing([3, 3])
	b4 = Bing([3, 4])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 新近在咫尺:
def XJZZC():
	# caoCao:
	caoCao = CaoCao([0, 3])
	# Jiangs:
	zhaoYun = Jiang([2, 2], VER, 'y')
	guanYu = Jiang([0, 1], HOR, 'g')
	maChao = Jiang([3, 0], VER, 'm')
	huangZhong = Jiang([2, 0], VER, 'h')
	zhangFei = Jiang([3, 2], VER, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([0, 2])
	b2 = Bing([1, 2])
	b3 = Bing([2, 4])
	b4 = Bing([3, 4])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 星罗棋布:
def XLQB():
	# caoCao:
	caoCao = CaoCao([1, 2])
	# Jiangs:
	zhaoYun = Jiang([1, 4], HOR, 'y')
	guanYu = Jiang([1, 0], HOR, 'g')
	maChao = Jiang([3, 1], VER, 'm')
	huangZhong = Jiang([0, 1], VER, 'h')
	zhangFei = Jiang([1, 1], HOR, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([0, 0])
	b2 = Bing([3, 0])
	b3 = Bing([0, 3])
	b4 = Bing([3, 3])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 四面八方:
def SMBF():
	# caoCao:
	caoCao = CaoCao([1, 2])
	# Jiangs:
	zhaoYun = Jiang([1, 4], HOR, 'y')
	guanYu = Jiang([1, 0], HOR, 'g')
	maChao = Jiang([3, 2], VER, 'm')
	huangZhong = Jiang([0, 2], VER, 'h')
	zhangFei = Jiang([1, 1], HOR, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([0, 1])
	b2 = Bing([3, 1])
	b3 = Bing([0, 4])
	b4 = Bing([3, 4])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 牛气冲天:
def NQCT():
	# caoCao:
	caoCao = CaoCao([1, 2])
	# Jiangs:
	zhaoYun = Jiang([1, 4], HOR, 'y')
	guanYu = Jiang([0, 1], HOR, 'g')
	maChao = Jiang([3, 2], VER, 'm')
	huangZhong = Jiang([0, 2], VER, 'h')
	zhangFei = Jiang([2, 1], HOR, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([0, 0])
	b2 = Bing([3, 0])
	b3 = Bing([0, 4])
	b4 = Bing([3, 4])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 调兵谴将:
def DBQJ():
	# caoCao:
	caoCao = CaoCao([0, 0])
	# Jiangs:
	zhaoYun = Jiang([0, 3], HOR, 'y')
	guanYu = Jiang([0, 2], HOR, 'g')
	maChao = Jiang([2, 3], HOR, 'm')
	huangZhong = Jiang([1, 4], HOR, 'h')
	zhangFei = Jiang([2, 2], HOR, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([2, 0])
	b2 = Bing([3, 0])
	b3 = Bing([2, 1])
	b4 = Bing([3, 1])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)

# 背水列阵:
def BSLZ():
	# caoCao:
	caoCao = CaoCao([1, 2])
	# Jiangs:
	zhaoYun = Jiang([2, 4], HOR, 'y')
	guanYu = Jiang([1, 0], HOR, 'g')
	maChao = Jiang([3, 0], VER, 'm')
	huangZhong = Jiang([0, 0], VER, 'h')
	zhangFei = Jiang([0, 4], HOR, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([1, 1])
	b2 = Bing([2, 1])
	b3 = Bing([0, 3])
	b4 = Bing([3, 3])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)


# 横刀立马2:
def HDLM2():
	# caoCao:
	caoCao = CaoCao([1, 0])
	# Jiangs:
	zhaoYun = Jiang([0, 3], VER, 'y')
	guanYu = Jiang([1, 2], HOR, 'g')
	maChao = Jiang([3, 0], VER, 'm')
	huangZhong = Jiang([0, 0], VER, 'h')
	zhangFei = Jiang([3, 3], VER, 'z')
	jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
	# Bings:
	b1 = Bing([0, 2])
	b2 = Bing([1, 3])
	b3 = Bing([2, 3])
	b4 = Bing([3, 2])
	bingList = [b1, b2, b3, b4]
	return Zhen(caoCao, jiangList, bingList)