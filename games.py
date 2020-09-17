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

# 比翼横飞:
def BYHF():
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