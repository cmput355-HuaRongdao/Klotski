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

	# according to the objects' information, fill in the huarongdao data structure the characters
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

class Zhen:
	def __init__(self, caoCao, jiangList, bingList):
		self.caoCao = caoCao
		self.jiangList = jiangList
		self.bingList = bingList

	def __eq__(self, other):
		if not isinstance(other, Zhen):
			return NotImplemented
		if not (self.caoCao == other.caoCao):
			return False
		for i in range(len(self.jiangList)):
			if not (self.jiangList[i] == other.jiangList[i]):
				return False
		for i in range(len(self.bingList)):
			if not (self.bingList[i] == other.bingList[i]):
				return False
		return True

# the characters:
class CaoCao:
	def __init__(self, position):
		self.position = position

	def __eq__(self, other):
		if not isinstance(other, CaoCao):
			return NotImplemented
		if not (self.position == other.position):
			return False
		return True

class Jiang:
	def __init__(self, position, orientation, name):
		self.position = position
		self.orientation = orientation
		self.name = name

	def __eq__(self, other):
		if not isinstance(other, Jiang):
			return NotImplemented
		if not (self.position == other.position):
			return False
		if not (self.orientation == other.orientation):
			return False
		return True


class Bing:
	def __init__(self, position):
		self.position = position

	def __eq__(self, other):
		if not isinstance(other, Bing):
			return NotImplemented
		if not (self.position == other.position):
			return False
		return True