# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
from solver import *

def bfs_game(zhen, title):
	# solve the puzzle:
	start_time = time.time()
	zhen = Search_Solver(zhen).bfs()
	elapsed_time = time.time() - start_time
	# get the solution path:
	path = [zhen]
	while zhen.getParent() is not None:
		zhen = zhen.getParent()
		path.append(zhen)
	# reverse the path:
	path.reverse()
	hrd = Huarongdao(path[0])
	# write down the results:
	f = open("./search_solutions/" + title + ".txt", 'w')
	f.write('================================================\n')
	f.write('=========' + title + ' by BFS ===================\n')
	f.write('================================================\n')
	# display the puzzle:
	for i in range(5):
		for j in range(4):
			f.write(hrd.hrd[j][i] + '  ')
		f.write('\n')
	f.write('\n')
	f.write('========= Solution =============================\n')
	f.write('Total number of steps: ' + str(len(path) - 1) + '\n')
	f.write('Total time used: ' + str(elapsed_time) + '\n')
	for state in path:
		hrd.buZhen(state)
		for i in range(5):
			for j in range(4):
				f.write(hrd.hrd[j][i] + '  ')
			f.write('\n')
		f.write('\n')
	f.close()

def a_star_game(zhen, title):
	#  500,solve the puzzle:
	start_time = time.time()
	zhen = Search_Solver(zhen).a_star()
	elapsed_time = time.time() - start_time
	# get the solution path:
	path = [zhen]
	while zhen.getParent() is not None:
		zhen = zhen.getParent()
		path.append(zhen)
	# reverse the path:
	path.reverse()
	hrd = Huarongdao(path[0])
	# write down the results:
	f = open("./search_solutions/" + title + ".txt", 'w')
	f.write('================================================\n')
	f.write('=========' + title + ' by A* =========================\n')
	f.write('================================================\n')
	# display the puzzle:
	for i in range(5):
		for j in range(4):
			f.write(hrd.hrd[j][i] + '  ')
		f.write('\n')
	f.write('\n')
	f.write('========= Solution =============================\n')
	f.write('Total number of steps: ' + str(len(path) - 1) + '\n')
	f.write('Total time used: ' + str(elapsed_time) + '\n')
	for state in path:
		hrd.buZhen(state)
		for i in range(5):
			for j in range(4):
				f.write(hrd.hrd[j][i] + '  ')
			f.write('\n')
		f.write('\n')
	f.close()

def sarsa_game(hrd, num_episodes, title):
	# specify the memory:
	memoryPath = './rl_training_results/sarsa/td_sarsa_savt' + title + '.txt'
	# solve the puzzle:
	start_time = time.time()
	result = RL_Solver(hrd, num_episodes).sarsa(memoryPath)
	elapsed_time = time.time() - start_time
	# get the solution path:
	zhen = result[1]
	path = [zhen]
	while zhen.getParent() is not None:
		zhen = zhen.getParent()
		path.append(zhen)
	# reverse the path:
	path.reverse()
	hrd = Huarongdao(path[0])
	# write down the results:
	f = open("./rl_solutions/sarsa/" + title + ".txt", 'w')
	f.write('================================================\n')
	f.write('=========' + title + ' by sarsa ======================\n')
	if result[2]:
		f.write('succeeded!\n')
	else:
		f.write('NOT successful......\n')
	f.write('the return for each episode: ' + str(result[0]) + '\n')
	f.write('================================================\n')
	# display the puzzle:
	for i in range(5):
		for j in range(4):
			f.write(hrd.hrd[j][i] + '  ')
		f.write('\n')
	f.write('\n')
	f.write('========= Solution =============================\n')
	f.write('Total number of steps: ' + str(len(path) - 1) + '\n')
	f.write('Total time used: ' + str(elapsed_time) + '\n')
	for state in path:
		hrd.buZhen(state)
		for i in range(5):
			for j in range(4):
				f.write(hrd.hrd[j][i] + '  ')
			f.write('\n')
		f.write('\n')
	f.close()

def q_learning_game(hrd, num_episodes, title):
	# specify the memory:
	memoryPath = './rl_training_results/q_learning/td_q_learning_savt' + title + '.txt'
	# solve the puzzle:
	start_time = time.time()
	result = RL_Solver(hrd, num_episodes).q_learning(memoryPath)
	elapsed_time = time.time() - start_time
	# get the solution path:
	zhen = result[1]
	path = [zhen]
	while zhen.getParent() is not None:
		zhen = zhen.getParent()
		path.append(zhen)
	# reverse the path:
	path.reverse()
	hrd = Huarongdao(path[0])
	# write down the results:
	f = open("./rl_solutions/q_learning/" + title + ".txt", 'w')
	f.write('================================================\n')
	f.write('=========' + title + ' by Q_learning ======================\n')
	if result[2]:
		f.write('succeeded!\n')
	else:
		f.write('NOT successful......\n')
	f.write('the return for each episode: ' + str(result[0]) + '\n')
	f.write('================================================\n')
	# display the puzzle:
	for i in range(5):
		for j in range(4):
			f.write(hrd.hrd[j][i] + '  ')
		f.write('\n')
	f.write('\n')
	f.write('========= Solution =============================\n')
	f.write('Total number of steps: ' + str(len(path) - 1) + '\n')
	f.write('Total time used: ' + str(elapsed_time) + '\n')
	for state in path:
		hrd.buZhen(state)
		for i in range(5):
			for j in range(4):
				f.write(hrd.hrd[j][i] + '  ')
			f.write('\n')
		f.write('\n')
	f.close()

def RTHS_game(hrd, num_episodes, title):
	# specify the memory:
	memoryPath = './rths_training_results/realtime_heuristic' + title + '.txt'
	# solve the puzzle:
	start_time = time.time()
	result = RTHS_Solver(hrd, num_episodes).real_time_heuristic_search(memoryPath)
	elapsed_time = time.time() - start_time
	# get the solution path:
	zhen = result[1]
	path = [zhen]
	while zhen.getParent() is not None:
		zhen = zhen.getParent()
		path.append(zhen)
	# reverse the path:
	path.reverse()
	hrd = Huarongdao(path[0])
	# write down the results:
	f = open("./rths_solutions/" + title + ".txt", 'w')
	f.write('================================================\n')
	f.write('=========' + title + ' by RTHS ======================\n')
	if result[2]:
		f.write('succeeded!\n')
	else:
		f.write('NOT successful......\n')
	f.write('the return for each episode: ' + str(result[0]) + '\n')
	f.write('================================================\n')
	# display the puzzle:
	for i in range(5):
		for j in range(4):
			f.write(hrd.hrd[j][i] + '  ')
		f.write('\n')
	f.write('\n')
	f.write('========= Solution =============================\n')
	f.write('Total number of steps: ' + str(len(path) - 1) + '\n')
	f.write('Total time used: ' + str(elapsed_time) + '\n')
	for state in path:
		hrd.buZhen(state)
		for i in range(5):
			for j in range(4):
				f.write(hrd.hrd[j][i] + '  ')
			f.write('\n')
		f.write('\n')
	f.close()

def main():
	start_time = time.time()
	'''
	# Zhen form:
	zhen = TZYY()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game1')
	print('finished Game1')
	# Zhen form:
	zhen = WHZJ()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game2')
	print('finished Game2')
	# Zhen form:
	zhen = JDHL()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game3')
	print('finished Game3')
	# Zhen form:
	zhen = QHHY()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game4')
	print('finished Game4')
	# Zhen form:
	zhen = BYHK()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game5')
	print('finished Game5')
	# Zhen form:
	zhen = QGWG()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game6')
	print('finished Game6')
	# Zhen form:
	zhen = WJBG()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game7')
	print('finished Game7')
	# Zhen form:
	zhen = BLCY()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game8')
	print('finished Game8')
	# Zhen form:
	zhen = SJLG()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game9')
	print('finished Game9')
	# Zhen form:
	zhen = XJZZC()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game10')
	print('finished Game10')
	'''
	# Zhen form:
	zhen = XLQB()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game11')
	print('finished Game11')
	# Zhen form:
	zhen = SMBF()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game12')
	print('finished Game12')
	# Zhen form:
	zhen = NQCT()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game13')
	print('finished Game13')
	# Zhen form:
	zhen = DBQJ()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game14')
	print('finished Game14')
	# Zhen form:
	zhen = BSZL()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game15')
	print('finished Game15')
	# Zhen form:
	zhen = HDLM2()	# from games.py
	bfs_game(Huarongdao(zhen), 'Game16')
	print('finished Game16')

	print('finished all!')
	time_elapsed = time.time() - start_time
	print('total time took: ', time_elapsed)

if __name__ == '__main__':
	main()