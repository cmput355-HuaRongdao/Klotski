# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
from util import *
from games import *
import copy

class Solver:
	zhenCollection = []
	zhenHistory = []
	choiceHistory = []

	def __init__(self, hrd):
		self.hrd = hrd
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

	# TO-BE-DELETED:
	def displayZhens(self):
		#print('==========================================')
		print(len(self.zhenHistory))
		print(len(self.choiceHistory))
		h = Huarongdao(TZYY())	# the default zhen

		
		h.buZhen(self.zhenHistory[-1])
		h.display()
		print('')
		

		'''
		for zhen in self.zhenHistory:
			h.buZhen(zhen)
			h.display()
			print('')
		'''

		#print('==========================================')

	def solve(self):
		# this variable is set to true if it's not the first time the search is at this node
		recursed = False
		step_count = 0
		# while Cao Cao is not at the exit
		# do a DFS:
		while not self.isSuccess():
		#for j in range(4715):
			#self.displayZhens()	# FIX ME
			# gather available next zhens:
			nextZhens = self.getNextStatesByZhen(self.hrd.zhen)
			numOfNextZhens = len(nextZhens)
			# go to a next zhen:
			# case 1, make the next choice at this state:
			if recursed:
				if (self.choiceHistory[-1] == numOfNextZhens or 
				nextZhens[self.choiceHistory[-1]] in self.zhenCollection):
					if len(self.zhenHistory) == 1:
						print('No solution is found for this puzzle...')
						print('size of zhen collection: ', self.zhenCollection)
						print('step count: ', step_count)
						exit()
					# all paths explored for this node or if must recurse, recurse again:
					self.zhenHistory.pop()
					self.hrd.zhen = self.zhenHistory[-1]
					self.choiceHistory.pop()
					self.choiceHistory[-1] += 1
					recursed = True
				else:
					# go explore the next branch:
					choice = self.choiceHistory[-1]
					self.hrd.zhen = nextZhens[choice]
					self.zhenHistory.append(self.hrd.zhen)
					self.zhenCollection.append(self.hrd.zhen)
					recursed = False

			# case 2, first time down this path:
			elif numOfNextZhens > 0:
				flag = False
				for i in range(numOfNextZhens):
					if nextZhens[i] not in self.zhenCollection:
						self.choiceHistory.append(i)
						self.hrd.zhen = nextZhens[i]	# explore the chosen path
						self.zhenHistory.append(self.hrd.zhen)
						self.zhenCollection.append(self.hrd.zhen)
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
		return [step_count, len(self.zhenCollection)]

def main():
	# Zhen form:
	zhen = JDHL()	# from games.py
	# init the puzzle object:
	hrd = Huarongdao(zhen)
	# display the puzzle:
	hrd.display()
	print('')
	# solve the puzzle:
	step_count, zhenCollection = Solver(hrd).solve()
	# display solving result:
	print("success!")
	hrd.display()
	print('size of zhen collection: ', zhenCollection)
	print("total step count: ", step_count)

if __name__ == '__main__':
	main()