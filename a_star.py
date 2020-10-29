from util import *
from games import *
def A_Star_Solver(Solver):
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
		#print(self.choiceHistory)
		print('')
		
		'''
		for zhen in zhens:
			h.buZhen(zhen)
			h.display()
			print('')
		'''

	def heuristic(self, zhen):
		# heuristic is the manhatton distance between cao cao and the escape point
		return abs(zhen.caoCao.pos[0] - 1) + (3 - zhen.caoCao.pos[1])

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
			nextZhens.sort(key = self.heuristic)
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
					step_count -= 1
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
							step_count += 1
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
						step_count += 1
						recursed = False
						flag = True
						break
				if flag:
					# a new zhen is chosen apart from any old ones
					continue
				# go explore the next branch:
				self.choiceHistory[-1] += 1
				# all paths explored for this branch, recurse:
				self.zhenHistory.pop()
				self.hrd.zhen = self.zhenHistory[-1]
				step_count -= 1
				recursed = True
			# case 3, the search stucks and goal is not reached:
			else:
				# go explore the next branch:
				self.choiceHistory[-1] += 1
				# all paths explored for this branch, recurse:
				self.zhenHistory.pop()
				self.hrd.zhen = self.zhenHistory[-1]	# go to the previous state
				step_count -= 1
				recursed = True
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