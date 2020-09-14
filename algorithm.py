# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
from util import *
from games import *

class Solver:
	def __init__(self, huarongdao):
		self.huarongdao = huarongdao
		# establish the start vertex
		self.start = self.huarongdao.zhen

	def isSuccess(self):
		return self.zhen.caoCao.position == [2, 4]

	def solve(self):
		# while Cao Cao is not at the exit
		while !self.isSuccess():
			# gather available next states:
			# go to a next state
			

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