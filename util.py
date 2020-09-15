# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
# ori of Jiang objects:
HOR = 0
VER = 1

class Huarongdao:
	hrd = [['.' for i in range(5)] for j in range(4)]	# huarongdao is a 4x5 board
	def __init__(self, zhen):
		self.zhen = zhen
		self.buZhen(self.zhen)

	# according to the objects' information, fill in the hrd data structure the characters
	def buZhen(self, zhen):
		caoCaox = zhen.caoCao.pos[0]
		caoCaoy = zhen.caoCao.pos[1]
		self.hrd[caoCaox][caoCaoy] = '$'	# "$" represents caoCao
		self.hrd[caoCaox + 1][caoCaoy] = '$'
		self.hrd[caoCaox][caoCaoy + 1] = '$'
		self.hrd[caoCaox + 1][caoCaoy + 1] = '$'
		for i in range(5):	# there are in total 5 Jiangs
			jiang = zhen.jiangList[i]
			x, y = jiang.pos
			name = jiang.name
			self.hrd[x][y] = name
			if jiang.ori == HOR:	# the Jiang is placed horizontally
				self.hrd[x + 1][y] = name
			else:	# the Jiang is placed vertically
				self.hrd[x][y + 1] = name
		for i in range(4):	# there are in total 4 Bings
			x, y = zhen.bingList[i].pos
			self.hrd[x][y] = '@'	# @ represents a soldier

	def getEmptySpaces(self):
		emptySpaces = []
		for i in range(4):
			for j in range(5):
				if self.hrd[i][j] == '.':
					emptySpaces.append([i, j])
		return emptySpaces

	def getJiangByName(self, name):
		for jiang in self.zhen.jiangList:
			if jiang.name == name:
				return jiang

	def getBingByPos(self, pos):
		for bing in self.zhen.bingList:
			if bing.pos == pos:
				return bing

	def getNextStates(self):
		nextStates = []
		a, b = self.getEmptySpaces()	# will always be two empty spaces
		# see if the empties are together or separate:
		if (abs(a[0] - b[0]) == 1 and a[1] == b[1]):	# one empty beside another empty
			# see if CaoCao can move:
			if (a[1] >= 2 and self.hrd[a[0]][a[1] - 1] == '$' 
			and self.hrd[b[0]][b[1] - 1] == '$'):	# see if CaoCao can move down
				newState = copy.deepcopy(self.curState)
				newState.caoCao.pos[1] += 1	# can move down one
				nextStates.append(newState)
			elif (a[1] <= 2 and self.hrd[a[0]][a[1] + 1] == '$' 
			and self.hrd[b[0]][b[1] + 1] == '$'):	# see if CaoCao can move up
				newState = copy.deepcopy(self.curState)
				newState.caoCao.pos[1] -= 1	# can move up one
				nextStates.append(newState)
			# see if some Jiangs can move:
			if (a[1] >= 1 and self.hrd[a[0]][a[1] - 1] != '@' 
			and self.hrd[b[0]][b[1] - 1] != '@' 
			and self.hrd[a[0]][a[1] - 1] == self.hrd[b[0]][b[1] - 1]):	# see if jiang can move down
				name = self.hrd[a[0]][a[1] - 1]
				newState = copy.deepcopy(self.curState)
				newState.getJiangByName(name).pos[1] += 1	# can move down one
				nextStates.append(newState)
			elif (a[1] <= 4 and self.hrd[a[0]][a[1] + 1] != '@' 
			and self.hrd[b[0]][b[1] + 1] != '@' 
			and self.hrd[a[0]][a[1] + 1] == self.hrd[b[0]][b[1] + 1]):	# see if jiang can move up
				name = self.hrd[a[0]][a[1] + 1]
				newState = copy.deepcopy(self.curState)
				newState.getJiangByName(name).pos[1] -= 1	# can move up one
				nextStates.append(newState)
		elif (abs(a[1] - b[1]) == 1 and a[0] == b[0]):	# one empty above another empty
			# see if CaoCao can move:
			if (a[0] >= 2 and self.hrd[a[0] - 1][a[1]] == '$' 
			and self.hrd[b[0] - 1][b[1]] == '$'):	# see if CaoCao can move right
				newState = copy.deepcopy(self.curState)
				newState.caoCao.pos[0] += 1	# can move right one
				nextStates.append(newState)
			elif (a[0] <= 1 and self.hrd[a[0] + 1][a[1]] == '$' 
			and self.hrd[b[0] + 1][b[1]] == '$'):	# see if CaoCao can move left
				newState = copy.deepcopy(self.curState)
				newState.caoCao.pos[0] -= 1	# can move left one
				nextStates.append(newState)
			# see if some Jiangs can move:
			if (a[0] >= 1 and self.hrd[a[0] - 1][a[1]] != '@' 
			and self.hrd[b[0] - 1][b[1]] != '@' 
			and self.hrd[a[0] - 1][a[1]] == self.hrd[b[0] - 1][b[1]]):	# see if jiang can move right
				name = self.hrd[a[0] - 1][a[1]]
				newState = copy.deepcopy(self.curState)
				newState.getJiangByName(name).pos[0] += 1	# can move right one
				nextStates.append(newState)
			elif (a[0] <= 2 and self.hrd[a[0] + 1][a[1]] != '@' 
			and self.hrd[b[0] + 1][b[1]] != '@' 
			and self.hrd[a[0] + 1][a[1]] == self.hrd[b[0] + 1][b[1]]):	# see if jiang can move left
				name = self.hrd[a[0] + 1][a[1]]
				newState = copy.deepcopy(self.curState)
				newState.getJiangByName(name).pos[0] -= 1	# can move left one
				nextStates.append(newState)
		# if the empties are separated:
		for p in [a, b]:
			# see if some Jiangs can move:
			if p[1] >= 2 and self.hrd[p[0]][p[1] - 1] not in ['@', '$', '.']:	# see if jiang can move down
				name = self.hrd[p[0]][p[1] - 1]
				jiang = self.curState.getJiangByName(name)
				if jiang.ori == VER:
					newState = copy.deepcopy(self.curState)
					newState.getJiangByName(name).pos[1] += 1	# can move down one
					nextStates.append(newState)
			elif p[1] <= 2 and self.hrd[p[0]][p[1] + 1] not in ['@', '$', '.']:	# see if jiang can move up
				name = self.hrd[p[0]][p[1] + 1]
				jiang = self.curState.getJiangByName(name)
				if jiang.ori == VER:
					newState = copy.deepcopy(self.curState)
					newState.getJiangByName(name).pos[1] -= 1	# can move up one
					nextStates.append(newState)
			if p[0] >= 2 and self.hrd[p[0] - 1][p[1]] not in ['@', '$', '.']:	# see if jiang can move right
				name = self.hrd[p[0] - 1][p[1]]
				jiang = self.curState.getJiangByName(name)
				if jiang.ori == HOR:
					newState = copy.deepcopy(self.curState)
					newState.getJiangByName(name).pos[0] += 1	# can move right one
					nextStates.append(newState)
			elif p[0] <= 1 and self.hrd[p[0] + 1][p[1]] not in ['@', '$', '.']:	# see if jiang can move left
				name = self.hrd[p[0] + 1][p[1]]
				jiang = self.curState.getJiangByName(name)
				if jiang.ori == HOR:
					newState = copy.deepcopy(self.curState)
					newState.getJiangByName(name).pos[0] -= 1	# can move left one
					nextStates.append(newState)
			# see if some bings can move:
			if p[1] >= 1 and self.hrd[p[0]][p[1] - 1] == '@':	# see if bing can move down
				newState = copy.deepcopy(self.curState)
				newState.getBingByPos(p).pos[1] += 1	# can move down one
				nextStates.append(newState)
			elif p[1] <= 3 and self.hrd[p[0]][p[1] + 1] == '@':	# see if bing can move up
				newState = copy.deepcopy(self.curState)
				newState.getBingByPos(p).pos[1] -= 1	# can move up one
				nextStates.append(newState)
			if p[0] >= 1 and self.hrd[p[0] - 1][p[1]] == '@':	# see if bing can move right
				newState = copy.deepcopy(self.curState)
				newState.getBingByPos(p).pos[0] += 1	# can move right one
				nextStates.append(newState)
			elif p[0] <= 2 and self.hrd[p[0] + 1][p[1]] == '@':	# see if bing can move left
				newState = copy.deepcopy(self.curState)
				newState.getBingByPos(p).pos[0] -= 1	# can move left one
				nextStates.append(newState)

	# displays the board to the terminal
	def display(self):
		for i in range(5):
			for j in range(4):
				print(self.hrd[j][i] + '  ', end = '')
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
	def __init__(self, pos):
		self.pos = pos

	def __eq__(self, other):
		if not isinstance(other, CaoCao):
			return NotImplemented
		if not (self.pos == other.pos):
			return False
		return True

class Jiang:
	def __init__(self, pos, ori, name):
		self.pos = pos
		self.ori = ori
		self.name = name

	def __eq__(self, other):
		if not isinstance(other, Jiang):
			return NotImplemented
		if not (self.pos == other.pos):
			return False
		if not (self.ori == other.ori):
			return False
		return True


class Bing:
	def __init__(self, pos):
		self.pos = pos
		self.id = id(self)

	def __eq__(self, other):
		if not isinstance(other, Bing):
			return NotImplemented
		if not (self.pos == other.pos):
			return False
		return True