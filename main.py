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
	bfs_game(Huarongdao(zhen), 'game_1')
	print('finished game_1')
	# Zhen form:
	zhen = WHZJ()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_2')
	print('finished game_2')
	# Zhen form:
	zhen = JDHL()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_3')
	print('finished game_3')
	# Zhen form:
	zhen = QHHY()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_4')
	print('finished game_4')
	# Zhen form:
	zhen = BYHK()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_5')
	print('finished game_5')
	# Zhen form:
	zhen = QGWG()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_6')
	print('finished game_6')
	# Zhen form:
	zhen = WJBG()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_7')
	print('finished game_7')
	# Zhen form:
	zhen = BLCY()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_8')
	print('finished game_8')
	# Zhen form:
	zhen = SJLG()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_9')
	print('finished game_9')
	# Zhen form:
	zhen = XJZZC()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_10')
	print('finished game_10')
	'''
	# Zhen form:
	zhen = XLQB()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_11')
	print('finished game_11')
	# Zhen form:
	zhen = SMBF()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_12')
	print('finished game_12')
	# Zhen form:
	zhen = NQCT()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_13')
	print('finished game_13')
	# Zhen form:
	zhen = DBQJ()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_14')
	print('finished game_14')
	# Zhen form:
	zhen = BSZL()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_15')
	print('finished game_15')
	# Zhen form:
	zhen = HDLM2()	# from games.py
	bfs_game(Huarongdao(zhen), 'game_16')
	print('finished game_16')

	print('finished all!')
	time_elapsed = time.time() - start_time
	print('total time took: ', time_elapsed)

if __name__ == '__main__':
	main()