# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
import copy
# ori. of Jiang objects:
HOR = 0
VER = 1

class Huarongdao(object):
	def __init__(self, zhen = None):
		self.zhen = zhen
		self.buZhen(self.zhen)

	# according to the objects' information, fill in the hrd data structure the characters
	def buZhen(self, zhen):
		self.hrd = [['.' for i in range(5)] for j in range(4)]	# huarongdao is a 4x5 board
		if zhen is None: return
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

	def getNextStatesAndSetParent(self, parent):
		# Note: this method is run based on the hrd data structure
		# this method can only be used after buZhen(self, zhen) is called
		nextStates = []
		a, b = self.getEmptySpaces()	# will always be two empty spaces
		# see if the empties are together or separate:
		if (abs(a[0] - b[0]) == 1 and a[1] == b[1]):	# one empty beside another empty
			# see if CaoCao can move:
			if (a[1] >= 2 and self.hrd[a[0]][a[1] - 1] == '$' 
			and self.hrd[b[0]][b[1] - 1] == '$'):	# see if CaoCao can move down
				newState = copy.deepcopy(self.zhen)
				newState.caoCao.pos[1] += 1	# can move down one
				newState.setParent(parent)
				nextStates.append(newState)
			if (a[1] <= 2 and self.hrd[a[0]][a[1] + 1] == '$' 
			and self.hrd[b[0]][b[1] + 1] == '$'):	# see if CaoCao can move up
				newState = copy.deepcopy(self.zhen)
				newState.caoCao.pos[1] -= 1	# can move up one
				newState.setParent(parent)
				nextStates.append(newState)
			# see if some Jiangs can move:
			if (a[1] >= 1 and self.hrd[a[0]][a[1] - 1] not in ['@', '$'] 
			and self.hrd[b[0]][b[1] - 1] != '@' 
			and self.hrd[a[0]][a[1] - 1] == self.hrd[b[0]][b[1] - 1]):	# see if jiang can move down
				name = self.hrd[a[0]][a[1] - 1]
				newState = copy.deepcopy(self.zhen)
				newState.getJiangByName(name).pos[1] += 1	# can move down one
				newState.setParent(parent)
				nextStates.append(newState)
			if (a[1] <= 3 and self.hrd[a[0]][a[1] + 1] not in ['@', '$'] 
			and self.hrd[b[0]][b[1] + 1] != '@' 
			and self.hrd[a[0]][a[1] + 1] == self.hrd[b[0]][b[1] + 1]):	# see if jiang can move up
				name = self.hrd[a[0]][a[1] + 1]
				newState = copy.deepcopy(self.zhen)
				newState.getJiangByName(name).pos[1] -= 1	# can move up one
				newState.setParent(parent)
				nextStates.append(newState)
		elif (abs(a[1] - b[1]) == 1 and a[0] == b[0]):	# one empty above another empty
			# see if CaoCao can move:
			if (a[0] >= 2 and self.hrd[a[0] - 1][a[1]] == '$' 
			and self.hrd[b[0] - 1][b[1]] == '$'):	# see if CaoCao can move right
				newState = copy.deepcopy(self.zhen)
				newState.caoCao.pos[0] += 1	# can move right one
				newState.setParent(parent)
				nextStates.append(newState)
			if (a[0] <= 1 and self.hrd[a[0] + 1][a[1]] == '$' 
			and self.hrd[b[0] + 1][b[1]] == '$'):	# see if CaoCao can move left
				newState = copy.deepcopy(self.zhen)
				newState.caoCao.pos[0] -= 1	# can move left one
				newState.setParent(parent)
				nextStates.append(newState)
			# see if some Jiangs can move:
			if (a[0] >= 1 and self.hrd[a[0] - 1][a[1]] not in ['@', '$']  
			and self.hrd[b[0] - 1][b[1]] != '@' 
			and self.hrd[a[0] - 1][a[1]] == self.hrd[b[0] - 1][b[1]]):	# see if jiang can move right
				name = self.hrd[a[0] - 1][a[1]]
				newState = copy.deepcopy(self.zhen)
				newState.getJiangByName(name).pos[0] += 1	# can move right one
				newState.setParent(parent)
				nextStates.append(newState)
			if (a[0] <= 2 and self.hrd[a[0] + 1][a[1]] not in ['@', '$']  
			and self.hrd[b[0] + 1][b[1]] != '@' 
			and self.hrd[a[0] + 1][a[1]] == self.hrd[b[0] + 1][b[1]]):	# see if jiang can move left
				name = self.hrd[a[0] + 1][a[1]]
				newState = copy.deepcopy(self.zhen)
				newState.getJiangByName(name).pos[0] -= 1	# can move left one
				newState.setParent(parent)
				nextStates.append(newState)
		# if the empties are separated:
		for p in [a, b]:
			# see if some Jiangs can move:
			if p[1] >= 2 and self.hrd[p[0]][p[1] - 1] not in ['@', '$', '.']:	# see if jiang can move down
				name = self.hrd[p[0]][p[1] - 1]
				jiang = self.zhen.getJiangByName(name)
				if jiang.ori == VER:
					newState = copy.deepcopy(self.zhen)
					newState.getJiangByName(name).pos[1] += 1	# can move down one
					newState.setParent(parent)
					nextStates.append(newState)
			if p[1] <= 2 and self.hrd[p[0]][p[1] + 1] not in ['@', '$', '.']:	# see if jiang can move up
				name = self.hrd[p[0]][p[1] + 1]
				jiang = self.zhen.getJiangByName(name)
				if jiang.ori == VER:
					newState = copy.deepcopy(self.zhen)
					newState.getJiangByName(name).pos[1] -= 1	# can move up one
					newState.setParent(parent)
					nextStates.append(newState)
			if p[0] >= 2 and self.hrd[p[0] - 1][p[1]] not in ['@', '$', '.']:	# see if jiang can move right
				name = self.hrd[p[0] - 1][p[1]]
				jiang = self.zhen.getJiangByName(name)
				if jiang.ori == HOR:
					newState = copy.deepcopy(self.zhen)
					newState.getJiangByName(name).pos[0] += 1	# can move right one
					newState.setParent(parent)
					nextStates.append(newState)
			if p[0] <= 1 and self.hrd[p[0] + 1][p[1]] not in ['@', '$', '.']:	# see if jiang can move left
				name = self.hrd[p[0] + 1][p[1]]
				jiang = self.zhen.getJiangByName(name)
				if jiang.ori == HOR:
					newState = copy.deepcopy(self.zhen)
					newState.getJiangByName(name).pos[0] -= 1	# can move left one
					newState.setParent(parent)
					nextStates.append(newState)
			# see if some bings can move:
			if p[1] >= 1 and self.hrd[p[0]][p[1] - 1] == '@':	# see if bing can move down
				newState = copy.deepcopy(self.zhen)
				newState.getBingByPos([p[0], p[1] - 1]).pos[1] += 1	# can move down one
				newState.setParent(parent)
				nextStates.append(newState)
			if p[1] <= 3 and self.hrd[p[0]][p[1] + 1] == '@':	# see if bing can move up
				newState = copy.deepcopy(self.zhen)
				newState.getBingByPos([p[0], p[1] + 1]).pos[1] -= 1	# can move up one
				newState.setParent(parent)
				nextStates.append(newState)
			if p[0] >= 1 and self.hrd[p[0] - 1][p[1]] == '@':	# see if bing can move right
				newState = copy.deepcopy(self.zhen)
				newState.getBingByPos([p[0] - 1, p[1]]).pos[0] += 1	# can move right one
				newState.setParent(parent)
				nextStates.append(newState)
			if p[0] <= 2 and self.hrd[p[0] + 1][p[1]] == '@':	# see if bing can move left
				newState = copy.deepcopy(self.zhen)
				newState.getBingByPos([p[0] + 1, p[1]]).pos[0] -= 1	# can move left one
				newState.setParent(parent)
				nextStates.append(newState)
		return nextStates

	# displays the board to the terminal
	def display(self):
		for i in range(5):
			for j in range(4):
				print(self.hrd[j][i] + '  ', end = '')
			print('')

class Zhen:
	def __init__(self, caoCao, jiangList, bingList, parent = None):
		self.parent = parent
		if self.parent is not None:
			self.cost = self.parent.getCost() + 1
		else:
			self.cost = 0
		self.caoCao = caoCao
		self.jiangList = jiangList
		self.bingList = bingList

	def __lt__(self, other):
		return self.getFValue() < other.getFValue()

	def __eq__(self, other):
		if not isinstance(other, Zhen):
			return NotImplemented
		return other.getAbstract() == self.getAbstract()

	def __hash__(self):
		return hash(self.getAbstract())

	def getH(self):
		p = self.caoCao.pos
		return abs(p[0] - 1) + abs(p[1] - 3)

	def getFValue(self):
		return self.getH() + self.cost

	def setParent(self, parent):
		self.cost = parent.cost + 1
		self.parent = parent

	def getParent(self):
		return self.parent

	def getAbstract(self):
		# this function generalize all Jiangs to be the same on the board.
		board = [['.' for i in range(5)] for j in range(4)]	# huarongdao is a 4x5 board
		caoCaox = self.caoCao.pos[0]
		caoCaoy = self.caoCao.pos[1]
		board[caoCaox][caoCaoy] = '$'	# "$" represents caoCao
		board[caoCaox + 1][caoCaoy] = '$'
		board[caoCaox][caoCaoy + 1] = '$'
		board[caoCaox + 1][caoCaoy + 1] = '$'
		for i in range(5):	# there are in total 5 Jiangs
			jiang = self.jiangList[i]
			x, y = jiang.pos
			board[x][y] = '#'	# '#' represents Jiang object
			if jiang.ori == HOR:	# the Jiang is placed horizontally
				board[x + 1][y] = '#'
			else:	# the Jiang is placed vertically
				board[x][y + 1] = '#'
		for i in range(4):	# there are in total 4 Bings
			x, y = self.bingList[i].pos
			board[x][y] = '@'	# @ represents a soldier
		serial = ''
		for i in range(len(board)):
			for j in range(len(board[0])):
				serial += board[i][j]
		return serial

	def getJiangByName(self, name):
		# get the Jiao object by its name
		for jiang in self.jiangList:
			if jiang.name == name:
				return jiang

	def getBingByPos(self, pos):
		# get the Bing object by its position
		for bing in self.bingList:
			if bing.pos == pos:
				return bing

# the characters:
class CaoCao(object):
	def __init__(self, pos):
		self.pos = pos

	def __eq__(self, other):
		if not isinstance(other, CaoCao):
			return NotImplemented
		if not (self.pos == other.pos):
			return False
		return True

class Jiang(object):
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


class Bing(object):
	def __init__(self, pos):
		self.pos = pos
		self.id = id(self)

	def __eq__(self, other):
		if not isinstance(other, Bing):
			return NotImplemented
		if not (self.pos == other.pos):
			return False
		return True