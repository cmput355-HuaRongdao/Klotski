# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan

# orientation of Jiang objects:
HOR = 0
VER = 1

class Huarongdao:
	huarongdao = [['.' for i in range(5)] for j in range(4)]	# huarongdao is a 4x5 board
	def __init__(self, zhen):
		self.zhen = zhen
		self.buZhen()

	def buZhen(self):
		caoCaox = self.zhen.caoCao.position[0]
		caoCaoy = self.zhen.caoCao.position[1]
		self.huarongdao[caoCaox][caoCaoy] = '$'	# $ represents caoCao
		self.huarongdao[caoCaox + 1][caoCaoy] = '$'
		self.huarongdao[caoCaox][caoCaoy + 1] = '$'
		self.huarongdao[caoCaox + 1][caoCaoy + 1] = '$'

		for i in range(5):	# there are in total 5 Jiangs
			jiang = self.zhen.jiangList[i]
			x, y = jiang.position
			name = jiang.name
			self.huarongdao[x][y] = name
			if jiang.orientation == HOR:	# the Jiang is placed horizontally
				self.huarongdao[x + 1][y] = name
			else:	# the Jiang is placed vertically
				self.huarongdao[x][y + 1] = name
		for i in range(4):	# there are in total 4 Bings
			x, y = self.zhen.bingList[i].position
			self.huarongdao[x][y] = '@'	# @ represents a soldier

	# displays the board to the terminal
	def display(self):
		for i in range(5):
			for j in range(4):
				print(self.huarongdao[j][i] + '  ', end = '')
			print('')

	def emptyPos():
		ans = []
		for i in range(4):
			for j in range(5):
				if huarongdao[i][j] == '.':
					ans.append([i, j])
		return ans

	def isSuccess():
		return self.zhen.caoCao.position == [2, 4]

class Zhen:
	def __init__(self, caoCao, jiangList, bingList):
		self.caoCao = caoCao
		self.jiangList = jiangList
		self.bingList = bingList

# the characters:
class CaoCao:
	def __init__(self, position):
		self.position = position

class Jiang:
	def __init__(self, position, orientation, name):
		self.position = position
		self.orientation = orientation
		self.name = name

class Bing:
	def __init__(self, position):
		self.position = position


def main():
	# 比翼横飞:
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
	# Zhen form:
	zhen = Zhen(caoCao, jiangList, bingList)
	# init the puzzle object:
	huarongdao = Huarongdao(zhen)
	# display the puzzle:
	huarongdao.display();

if __name__ == '__main__':
	main()