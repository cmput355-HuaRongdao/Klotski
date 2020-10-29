# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan

from heapq import *
from games import *
import copy
import time

class Solver:
	def __init__(self, hrd):
		self.hrd = hrd
		self.zhenCollection = []	# stores the visited states

	# returns true is Cao Cao is at the escape point
	def isSuccess(self, cur_zhen):
		return cur_zhen.caoCao.pos == [1, 3]

	def getNextStatesByZhen(self, zhen):
		# current state's neighbors are returned with their parent attribute
		# set as the zhen object past in:
		self.hrd.zhen = zhen
		self.hrd.buZhen(zhen)
		nextStates = self.hrd.getNextStatesAndSetParent(zhen)
		return nextStates

	def addToZhenCollection(self, zhen):
		# generalize the state(zhen past in) to represent all of its equivalences,
		# and put it into the zhenCollection
		self.zhenCollection.append(zhen)

	def bfs(self):
		zhenSet = {self.hrd.zhen}
		# while Cao Cao is not at the exit
		# do a BFS:
		# gather available next zhens:
		self.addToZhenCollection(self.hrd.zhen)
		while len(self.zhenCollection) > 0:
			current_zhen = self.zhenCollection.pop(0)
			nextZhens = self.getNextStatesByZhen(current_zhen)	# parents of each state set here
			for state in nextZhens:
				# if the state is new, add it to the collection:
				if state not in zhenSet:
					if self.isSuccess(state):
						return state
					else:
						zhenSet.add(state)
						self.addToZhenCollection(state)

	def bfs_game(self, title):
		print('================================================')
		print('=========', title, ' by BFS =====================')
		print('================================================')
		# display the puzzle:
		self.hrd.display()
		print('')
		# solve the puzzle:
		start_time = time.time()
		zhen = self.bfs()
		elapsed_time = time.time() - start_time
		# get the solution path:
		path = [zhen]
		while zhen.getParent() is not None:
			zhen = zhen.getParent()
			path.append(zhen)
		# reverse the path:
		path.reverse()

		# write down the results:
		f = open("testFile.txt", 'w')
		f.write('================================================\n')
		f.write('=========' + title + ' by BFS ===================\n')
		f.write('================================================\n')
		# display the puzzle:
		for i in range(5):
			for j in range(4):
				f.write(self.hrd.hrd[j][i] + '  ')
			f.write('\n')
		f.write('\n')
		f.write('========= Solution =============================\n')
		f.write('Total number of steps: ' + str(len(path) - 1))
		f.write('Total time used: ' + str(elapsed_time))
		for state in path:
			self.hrd.buZhen(state)
			for i in range(5):
				for j in range(4):
					f.write(self.hrd.hrd[j][i] + '  ')
				f.write('')
			f.write('')
		f.close()

		# display the path:
		print('========= Solution =============================')
		print('Total number of steps: ', len(path) - 1)
		print('Total time used: ', elapsed_time)
		for state in path:
			self.hrd.buZhen(state)
			self.hrd.display()
			print('')

	def a_star(self):
		zhenSet = {self.hrd.zhen}
		heap = [(self.hrd.zhen.getFValue(), self.hrd.zhen)]
		# while Cao Cao is not at the exit
		# do a_star search:
		# gather available next zhens:
		while len(heap) > 0:
			current_zhen = heappop(heap)[1]
			nextZhens = self.getNextStatesByZhen(current_zhen)	# parents of each state set here
			for state in nextZhens:
				# if the state is new, add it to the collection:
				if state not in zhenSet:
					if self.isSuccess(state):
						return state
					else:
						zhenSet.add(state)
						heappush(heap, (state.getFValue(), state))

	def a_star_game(self, title):
		print('================================================')
		print('=========', title, ' by A* ======================')
		print('================================================')
		# display the puzzle:
		self.hrd.display()
		print('')
		# solve the puzzle:
		start_time = time.time()
		zhen = self.a_star()
		elapsed_time = time.time() - start_time
		# get the solution path:
		path = [zhen]
		while zhen.getParent() is not None:
			zhen = zhen.getParent()
			path.append(zhen)
		# reverse the path:
		path.reverse()

		# write down the results:
		f = open("testFile.txt", 'w')
		f.write('================================================\n')
		f.write('=========' + title + ' by A* =========================\n')
		f.write('================================================\n')
		# display the puzzle:
		for i in range(5):
			for j in range(4):
				f.write(self.hrd.hrd[j][i] + '  ')
			f.write('\n')
		f.write('\n')
		f.write('========= Solution =============================\n')
		f.write('Total number of steps: ' + str(len(path) - 1) + '\n')
		f.write('Total time used: ' + str(elapsed_time) + '\n')
		for state in path:
			self.hrd.buZhen(state)
			for i in range(5):
				for j in range(4):
					f.write(self.hrd.hrd[j][i] + '  ')
				f.write('\n')
			f.write('\n')
		f.close()


		# display the path:
		print('========= Solution =============================')
		print('Total number of steps: ', len(path) - 1)
		print('Total time used: ', elapsed_time)
		for state in path:
			self.hrd.buZhen(state)
			self.hrd.display()
			print('')

def main():
	'''
	# Zhen form:
	zhen = TZYY()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('逃之夭夭')
	# Zhen form:
	zhen = WHZJ()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('无横之局')
	# Zhen form:
	zhen = JDHL()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('将当后路')
	# Zhen form:
	zhen = QHHY()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('前呼后拥')
	# Zhen form:
	zhen = BYHK()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('比翼横空')
	# Zhen form:
	zhen = QGWG()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('巧过五关')
	# Zhen form:
	zhen = WJBG()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('五将逼宫')
	# Zhen form:
	zhen = BLCY()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('兵临曹营')
	# Zhen form:
	zhen = SJLG()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('四将连关')
	# Zhen form:
	zhen = XJZZC()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('新近在咫尺')
	# Zhen form:
	zhen = XLQB()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('星罗棋布')
	# Zhen form:
	zhen = SMBF()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('四面八方')
	'''
	# Zhen form:
	zhen = NQCT()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('牛气冲天')
	'''
	# Zhen form:
	zhen = DBQJ()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('调兵谴将')
	# Zhen form:
	zhen = BSZL()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('背水列阵')
	# Zhen form:
	zhen = HDLM2()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('横刀立马2')
	'''

if __name__ == '__main__':
	main()