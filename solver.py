# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
from heapq import *
from games import *
import copy
import time

class Search_Solver:
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
		self.hrd.buZhen(path[0])
		# write down the results:
		f = open("./solutions/" + title + ".txt", 'w')
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
		self.hrd.buZhen(path[0])
		# write down the results:
		f = open("./solutions/" + title + ".txt", 'w')
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