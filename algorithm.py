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

	# DEPRECATED:
	def dfs(self):
		zhenHistory = []	# stores the current paths
		choiceHistory = []	# for dfs only
		# add the first zhen into history
		# there is always one more element in zhenHistory than choiceHistory:
		zhenHistory.append(self.hrd.zhen)
		self.addToZhenCollection(self.hrd.zhen)
		# this variable is set to true if it's not the first time the search is at this node
		recursed = False
		step_count = 0
		# while Cao Cao is not at the exit
		# do a DFS:
		while not self.isSuccess(self.hrd.zhen):
			# gather available next zhens:
			nextZhens = self.getNextStatesByZhen(self.hrd.zhen)
			numOfNextZhens = len(nextZhens)
			# go to a next zhen:
			# case 1, make the next choice at this state:
			if recursed:
				if choiceHistory[-1] == numOfNextZhens: 
					if len(zhenHistory) == 1:
						print('No solution is found for this puzzle...')
						# update the data structure for displaying the result:
						self.hrd.buZhen(self.hrd.zhen)
						return [step_count, len(self.zhenCollection), choiceHistory,
						self.max_counter, self.max_len_history]
					# all paths explored for this node or if must recurse, recurse again:
					zhenHistory.pop()
					self.hrd.zhen = zhenHistory[-1]
					choiceHistory.pop()
					choiceHistory[-1] += 1
					recursed = True
				elif self.checkDup(nextZhens[choiceHistory[-1]]):
					choiceHistory[-1] += 1
					recursed = True
				else:
					# go explore the next branch:
					flag = False
					choice = choiceHistory[-1]
					for i in range(choice, numOfNextZhens):
						if not self.checkDup(nextZhens[i]):
							self.hrd.zhen = nextZhens[i]
							zhenHistory.append(self.hrd.zhen)
							self.addToZhenCollection(self.hrd.zhen)
							choiceHistory[-1] = i
							recursed = False
							flag = True
							break
					if flag: continue

			# case 2, first time down this path:
			elif numOfNextZhens > 0:
				flag = False
				for i in range(numOfNextZhens):
					if not self.checkDup(nextZhens[i]):
						choiceHistory.append(i)
						self.hrd.zhen = nextZhens[i]	# explore the chosen path
						zhenHistory.append(self.hrd.zhen)
						self.addToZhenCollection(self.hrd.zhen)
						recursed = False
						flag = True
						break
				if flag:
					# a new zhen is chosen apart from any old ones
					step_count += 1
					continue
				# go explore the next branch:
				choiceHistory[-1] += 1
				# all paths explored for this branch, recurse:
				zhenHistory.pop()
				self.hrd.zhen = zhenHistory[-1]
				recursed = True
			# case 3, the search stucks and goal is not reached:
			else:
				# go explore the next branch:
				choiceHistory[-1] += 1
				# all paths explored for this branch, recurse:
				zhenHistory.pop()
				self.hrd.zhen = zhenHistory[-1]	# go to the previous state
				recursed = True
			# one step is taken
			step_count += 1
		# update the data structure for displaying the result:
		self.hrd.buZhen(self.hrd.zhen)
		print('success!')
		return [step_count, len(self.zhenCollection), choiceHistory]

	# DEPRECATED:
	def dfs_game(self, title):
		print('================================================')
		print('=========', title, '=============================')
		print('================================================')
		# display the puzzle:
		self.hrd.display()
		print('')
		# solve the puzzle:
		step_count, zhenCollectionSize, choiceHistory = self.dfs()
		# display solving result:
		self.hrd.display()
		print('choiceHistory: ', choiceHistory)
		print('size of choiceHistory: ', len(choiceHistory))
		print('size of zhen collection: ', zhenCollectionSize)
		print("total step count: ", step_count)

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
	Solver(Huarongdao(zhen)).bfs_game('逃之夭夭')
	# Zhen form:
	zhen = WHZJ()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('无横之局')
	# Zhen form:
	zhen = JDHL()	# from games.py
	Solver(Huarongdao(zhen)).bfs_game('将当后路')
	# Zhen form:
	zhen = QHHY()	# from games.py
	Solver(Huarongdao(zhen)).bfs_game('前呼后拥')
	# Zhen form:
	zhen = BYHK()	# from games.py
	Solver(Huarongdao(zhen)).bfs_game('比翼横空')
	# Zhen form:
	zhen = QGWG()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('巧过五关')
	# Zhen form:
	zhen = QGWG()	# from games.py
	Solver(Huarongdao(zhen)).bfs_game('巧过五关')
	# Zhen form:
	zhen = WJBG()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('五将逼宫')
	'''
	# Zhen form:
	zhen = HDLM2()	# from games.py
	Solver(Huarongdao(zhen)).a_star_game('横刀立马2')

if __name__ == '__main__':
	main()