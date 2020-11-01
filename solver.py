# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
import numpy as np
from heapq import *
from games import *
import copy
import time

class Solver(object):
	def __init__(self, hrd):
		self.hrd = hrd

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

class Search_Solver(Solver):
	def bfs(self):
		zhenSet = {self.hrd.zhen}
		zhenQueue = [self.hrd.zhen]
		# while Cao Cao is not at the exit
		# do a BFS:
		while len(zhenQueue) > 0:
			current_zhen = zhenQueue.pop(0)
			nextZhens = self.getNextStatesByZhen(current_zhen)	# parents of each state set here
			for state in nextZhens:
				# if the state is new, add it to the collection:
				if state not in zhenSet:
					if self.isSuccess(state):
						return state
					else:
						zhenSet.add(state)
						zhenQueue.append(state)

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

class RL_Solver(Solver):
	pass