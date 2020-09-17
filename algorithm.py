# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
from util import *
from games import *
import copy

class Solver:
	def __init__(self, hrd):
		self.hrd = hrd
		self.zhenCollection = []
		self.zhenHistory = []
		self.choiceHistory = []
		# add the first zhen into history
		# there is always one more element in zhenHistory than choiceHistory:
		self.zhenHistory.append(self.hrd.zhen)
		self.zhenCollection.append(self.hrd.zhen)

	# returns true is Cao Cao is at the escape point
	def isSuccess(self):
		return self.hrd.zhen.caoCao.pos == [1, 3]

	def getNextStatesByZhen(self, zhen):
		self.hrd.buZhen(zhen)
		return self.hrd.getNextStates()

	
	def abstractBuZhen(self, zhen):
		board = [['.' for i in range(5)] for j in range(4)]	# huarongdao is a 4x5 board
		caoCaox = zhen.caoCao.pos[0]
		caoCaoy = zhen.caoCao.pos[1]
		board[caoCaox][caoCaoy] = '$'	# "$" represents caoCao
		board[caoCaox + 1][caoCaoy] = '$'
		board[caoCaox][caoCaoy + 1] = '$'
		board[caoCaox + 1][caoCaoy + 1] = '$'
		for i in range(5):	# there are in total 5 Jiangs
			jiang = zhen.jiangList[i]
			x, y = jiang.pos
			board[x][y] = '#'	# '#' represents Jiang object
			if jiang.ori == HOR:	# the Jiang is placed horizontally
				board[x + 1][y] = '#'
			else:	# the Jiang is placed vertically
				board[x][y + 1] = '#'
		for i in range(4):	# there are in total 4 Bings
			x, y = zhen.bingList[i].pos
			board[x][y] = '@'	# @ represents a soldier
		return board

	def addToZhenCollection(self, zhen):
		self.zhenCollection.append(self.abstractBuZhen(zhen))

	def checkDup(self, zhen):
		return self.abstractBuZhen(zhen) in self.zhenCollection

	# TO-BE-DELETED:
	counter = 0
	max_len_history = 0
	max_counter = 0
	def displayZhens(self, zhens):
		self.counter += 1
		if len(self.choiceHistory) > self.max_len_history:
			self.max_len_history = len(self.choiceHistory)
			self.max_counter = self.counter

		print('================================================')
		h = Huarongdao(TZYY())	# the default zhen

		print(self.counter)

		h.buZhen(self.hrd.zhen)
		h.display()
		print('')

		print(len(self.zhenHistory))
		print(len(self.choiceHistory))
		print(self.choiceHistory)
		print('')
		
		'''
		for zhen in zhens:
			h.buZhen(zhen)
			h.display()
			print('')
		'''

	def solve(self):
		# this variable is set to true if it's not the first time the search is at this node
		recursed = False
		step_count = 0
		# while Cao Cao is not at the exit
		# do a DFS:
		while not self.isSuccess():
		#for j in range(29):
			# gather available next zhens:
			nextZhens = self.getNextStatesByZhen(self.hrd.zhen)
			#self.displayZhens(nextZhens)	# FIX ME
			numOfNextZhens = len(nextZhens)
			# go to a next zhen:
			# case 1, make the next choice at this state:
			if recursed:
				if self.choiceHistory[-1] == numOfNextZhens: 
					if len(self.zhenHistory) == 1:
						print('No solution is found for this puzzle...')
						# update the data structure for displaying the result:
						self.hrd.buZhen(self.hrd.zhen)
						return [step_count, len(self.zhenCollection), self.choiceHistory,
						self.max_counter, self.max_len_history]
					# all paths explored for this node or if must recurse, recurse again:
					self.zhenHistory.pop()
					self.hrd.zhen = self.zhenHistory[-1]
					self.choiceHistory.pop()
					self.choiceHistory[-1] += 1
					recursed = True
				elif self.checkDup(nextZhens[self.choiceHistory[-1]]):
					self.choiceHistory[-1] += 1
					recursed = True
				else:
					# go explore the next branch:
					flag = False
					choice = self.choiceHistory[-1]
					for i in range(choice, numOfNextZhens):
						if not self.checkDup(nextZhens[i]):
							self.hrd.zhen = nextZhens[i]
							self.zhenHistory.append(self.hrd.zhen)
							self.addToZhenCollection(self.hrd.zhen)
							self.choiceHistory[-1] = i
							recursed = False
							flag = True
							break
					if flag: continue

			# case 2, first time down this path:
			elif numOfNextZhens > 0:
				flag = False
				for i in range(numOfNextZhens):
					if not self.checkDup(nextZhens[i]):
						self.choiceHistory.append(i)
						self.hrd.zhen = nextZhens[i]	# explore the chosen path
						self.zhenHistory.append(self.hrd.zhen)
						self.addToZhenCollection(self.hrd.zhen)
						recursed = False
						flag = True
						break
				if flag:
					# a new zhen is chosen apart from any old ones
					step_count += 1
					continue
				# go explore the next branch:
				self.choiceHistory[-1] += 1
				# all paths explored for this branch, recurse:
				self.zhenHistory.pop()
				self.hrd.zhen = self.zhenHistory[-1]
				recursed = True
			# case 3, the search stucks and goal is not reached:
			else:
				# go explore the next branch:
				self.choiceHistory[-1] += 1
				# all paths explored for this branch, recurse:
				self.zhenHistory.pop()
				self.hrd.zhen = self.zhenHistory[-1]	# go to the previous state
				recursed = True
			# one step is taken
			step_count += 1
		# update the data structure for displaying the result:
		self.hrd.buZhen(self.hrd.zhen)
		print('success!')
		return [step_count, len(self.zhenCollection), self.choiceHistory]

	def game(self, title):
		print('================================================')
		print('=========', title, '=============================')
		print('================================================')
		# display the puzzle:
		self.hrd.display()
		print('')
		# solve the puzzle:
		step_count, zhenCollectionSize, choiceHistory = self.solve()
		# display solving result:
		self.hrd.display()
		print('choiceHistory: ', choiceHistory)
		print('size of choiceHistory: ', len(choiceHistory))
		print('size of zhen collection: ', zhenCollectionSize)
		print("total step count: ", step_count)

def main():
	'''
	# Zhen form:
	zhen = TZYY()	# from games.py
	Solver(Huarongdao(zhen)).game('逃之夭夭')
	# Zhen form:
	zhen = WHZJ()	# from games.py
	Solver(Huarongdao(zhen)).game('无横之局')
	# Zhen form:
	zhen = JDHL()	# from games.py
	Solver(Huarongdao(zhen)).game('将当后路')
	# Zhen form:
	zhen = QHHY()	# from games.py
	Solver(Huarongdao(zhen)).game('前呼后拥')
	# Zhen form:
	zhen = BYHK()	# from games.py
	Solver(Huarongdao(zhen)).game('比翼横空')
	# Zhen form:
	zhen = QGWG()	# from games.py
	Solver(Huarongdao(zhen)).game('巧过五关')
	# Zhen form:
	zhen = WJBG()	# from games.py
	Solver(Huarongdao(zhen)).game('五将逼宫')
	'''
	# Zhen form:
	zhen = HDLM2()	# from games.py
	Solver(Huarongdao(zhen)).game('横刀立马')

if __name__ == '__main__':
	main()