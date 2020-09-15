# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
from util import *
from games import *
import copy

class Solver:
	stateHistory = []
	choiceHistory = []
	def __init__(self, huarongdao):
		self.huarongdao = huarongdao
		self.curState = self.huarongdao.zhen
		# add the first state into history
		self.stateHistory.append(self.curState)

	# returns true is Cao Cao is at the escape point
	def isSuccess(self):
		return self.curState.caoCao.pos == [2, 4]



	def solve(self):
		# while Cao Cao is not at the exit
		while not self.isSuccess():
			# gather available next states:
			# go to a next state
			pass
			

def main():
	# Zhen form:
	zhen = TZYY()	# from games.py
	# init the puzzle object:
	huarongdao = Huarongdao(zhen)
	# display the puzzle:
	huarongdao.display();
	# solve the puzzle:
	Solver(huarongdao).solve()
	# display solving result:
	print("success!")
	huarongdao.display()

if __name__ == '__main__':
	main()