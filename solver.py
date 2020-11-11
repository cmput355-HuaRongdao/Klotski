# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
import numpy as np
from heapq import *
from games import *
import copy
import time
from rlagents import *
from util import *
import sys

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
		nextStates = self.hrd.getNextStates(zhen)
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
	def __init__(self, hrd, num_of_episodes = 20):
		self.hrd = hrd
		self.k = num_of_episodes	# k is the number of episodes
		self.start_state = self.hrd.zhen
		# set recursion limit:
		sys.setrecursionlimit(10**9)
		np.random.seed(0)

	def getNeighborsAndOrUpdateSavt(self, cur_state, savt):
		# returns the neighbors of cur_state as a
		# dictionary with keys being state and value being return
		if cur_state not in savt.savt:
			neighbors = self.getNextStatesByZhen(cur_state)
			savt.addNewStateActionSet(cur_state, {})
			for i in neighbors:
				savt.setStateActionValue(cur_state, i, 0)
		return savt.getAllNextStates(cur_state)

	def isDeadendReached(self, state):
		nextStates = self.getNextStatesByZhen(state)
		return (len(nextStates) == 1 and nextStates[0] == state.getParent());

	def getReturn(self, state, deadendReached):
		if self.isSuccess(state):
			# goal reached
			return 1000
		elif deadendReached:
			# a dead end has been reached
			return -1000
		else:
			# a normal step is taken
			return -1

	def sarsa(self, memoryPath):
		# load the previous memory:
		print('loading memory ......')
		savt = StateActionValueTable(memoryPath)	# load memory is also done here
		print('memory loaded!')
		rewardList = []
		# set up the agent:
		alpha = 0.5	# alpha is the step size
		gamma = 1
		agent = Sarsa_Agent(alpha, gamma)
		# want to save result every 10 episodes:
		temp_episode_count = 0
		# need a max_steps to save time:
		max_steps = 100 + self.k
		for i in range(self.k):
			if temp_episode_count >= 10:
				# save the learnt result:
				print('saving memory......')
				savt.saveStateActionValueTable(memoryPath)
				print('memory saved.')
				# reset episode count:
				temp_episode_count = 0
			print('doing episode ' + str(i + 1) + ' ......', end='')
			epsilon = 1 / (i + 1)
			agent.epsilon = epsilon
			# set up terminal conditions:
			deadend_count = 1	# terminate after a number of dead ends
			# set up initial conditions:
			ret_curepisode = 0
			cur_state = self.start_state
			steps_taken = 0
			while deadend_count > 0 and not self.isSuccess(cur_state) and steps_taken <= max_steps:
				# get the set of next states
				state_options = self.getNeighborsAndOrUpdateSavt(cur_state, savt)
				# let the agent select an action:
				next_state = agent.selectAction(state_options)	# here cur_action = next_state
				# observe the return of next state:
				deadendReached = self.isDeadendReached(next_state)
				if deadendReached:
					# deadend_count decrease by 1 if reached
					deadend_count -= 1
				ret = self.getReturn(next_state, deadendReached)
				ret_curepisode += ret
				# get next action:
				next_action = agent.selectAction(self.getNeighborsAndOrUpdateSavt(next_state, savt))
				# agent updates the state action value table:
				agent.updateActionValue(savt, cur_state, next_state, next_state, next_action, ret)
				# go to next state:
				cur_state = next_state
				steps_taken += 1
			# display reward after each episode:
			print('reward is ' + str(ret_curepisode))
			rewardList.append(ret_curepisode)
			# count episode:
			temp_episode_count += 1
			# decrement max_steps:
			max_steps -= 1
		# save the learnt result:
		print('saving memory......')
		savt.saveStateActionValueTable(memoryPath)
		print('memory saved.')
		return (rewardList, cur_state, self.isSuccess(cur_state))

	def q_learning(self, memoryPath):
		# load the previous memory:
		print('loading memory ......')
		savt = StateActionValueTable(memoryPath)	# load memory is also done here
		print('memory loaded!')
		rewardList = []
		# set up the agent:
		alpha = 0.5	# alpha is the step size
		gamma = 1
		agent = Q_Learning_Agent(alpha, gamma)
		# want to save result every 10 episodes:
		temp_episode_count = 0
		# need a max_steps to save time:
		max_steps = 100 + self.k
		for i in range(self.k):
			if temp_episode_count >= 10:
				# save the learnt result:
				print('saving memory......')
				savt.saveStateActionValueTable(memoryPath)
				print('memory saved.')
				# reset episode count:
				temp_episode_count = 0
			print('doing episode ' + str(i + 1) + ' ......', end='')
			epsilon = 1 / (i + 1)
			agent.epsilon = epsilon
			# set up terminal conditions:
			deadend_count = 1	# terminate after a number of dead ends
			# set up initial conditions:
			ret_curepisode = 0
			cur_state = self.start_state
			steps_taken = 0
			while deadend_count > 0 and not self.isSuccess(cur_state) and steps_taken <= max_steps:
				# get the set of next states
				state_options = self.getNeighborsAndOrUpdateSavt(cur_state, savt)
				# let the agent select an action:
				next_state = agent.selectAction(state_options)	# here cur_action = next_state
				# observe the return of next state:
				deadendReached = self.isDeadendReached(next_state)
				if deadendReached:
					# deadend_count decrease by 1 if reached
					deadend_count -= 1
				ret = self.getReturn(next_state, deadendReached)
				ret_curepisode += ret
				# get next action:
				next_action = agent.selectAction(self.getNeighborsAndOrUpdateSavt(next_state, savt))
				# agent updates the state action value table:
				opt_next_state = np.random.choice(agent.optimal_states(state_options))
				opt_next_action_set = self.getNeighborsAndOrUpdateSavt(opt_next_state, savt)
				opt_next_action = np.random.choice(agent.optimal_states(opt_next_action_set))
				agent.updateActionValue(savt, cur_state, next_state, opt_next_state, opt_next_action, ret)
				# go to next state:
				cur_state = next_state
				steps_taken += 1
			# display reward after each episode:
			print('reward is ' + str(ret_curepisode))
			rewardList.append(ret_curepisode)
			# count episode:
			temp_episode_count += 1
			# decrement max_steps:
			max_steps -= 1
		# save the learnt result:
		print('saving memory......')
		savt.saveStateActionValueTable(memoryPath)
		print('memory saved.')
		return (rewardList, cur_state, self.isSuccess(cur_state))

class RTHS_Solver(Solver):
	def __init__(self, hrd, num_of_episodes = 20):
		self.hrd = hrd
		self.k = num_of_episodes	# k is the number of episodes
		self.start_state = self.hrd.zhen
		np.random.seed(0)

	def real_time_heuristic_search(self, memoryPath):


				
