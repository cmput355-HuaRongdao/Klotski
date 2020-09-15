# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
from util import *
from games import *
import copy

class Solver:
	stateHistory = []
	choiceHistory = []
	def __init__(self, hrd):
		self.hrd = hrd
		self.curState = self.hrd.zhen
		# add the first state into history
		self.stateHistory.append(self.curState)

	# returns true is Cao Cao is at the escape point
	def isSuccess(self):
		return self.curState.caoCao.pos == [2, 4]

	def solve(self):
		nextStates = self.hrd.getNextStates()
		for state in nextStates:
			self.hrd.buZhen(state)
			self.hrd.display()
			print('')
		'''
		# while Cao Cao is not at the exit
		while not self.isSuccess():
			# gather available next states:
			# go to a next state
			pass
		'''
			

def main():
	# Zhen form:
	zhen = TZYY()	# from games.py
	# init the puzzle object:
	hrd = Huarongdao(zhen)
	# display the puzzle:
	hrd.display()
	print('')
	# solve the puzzle:
	Solver(hrd).solve()
	# display solving result:
	print("success!")
	#hrd.display()

if __name__ == '__main__':
	main()