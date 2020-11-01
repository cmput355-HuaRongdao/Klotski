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
	f = open("./solutions/" + title + ".txt", 'w')
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
	f.write('Total number of steps: ' + str(len(path) - 1))
	f.write('Total time used: ' + str(elapsed_time))
	for state in path:
		hrd.buZhen(state)
		for i in range(5):
			for j in range(4):
				f.write(hrd.hrd[j][i] + '  ')
			f.write('\n')
		f.write('\n')
	f.close()

def a_star_game(zhen, title):
	# solve the puzzle:
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
	f = open("./solutions/" + title + ".txt", 'w')
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

def main():
	start_time = time.time()
	'''
	# Zhen form:
	zhen = TZYY()	# from games.py
	a_star_game(Huarongdao(zhen), '逃之夭夭')
	print('finished 逃之夭夭')
	'''
	# Zhen form:
	zhen = WHZJ()	# from games.py
	a_star_game(Huarongdao(zhen), '无横之局')
	print('finished 无横之局')
	'''
	# Zhen form:
	zhen = JDHL()	# from games.py
	a_star_game(Huarongdao(zhen), '将当后路')
	print('finished 将当后路')
	# Zhen form:
	zhen = QHHY()	# from games.py
	a_star_game(Huarongdao(zhen), '前呼后拥')
	print('finished 前呼后拥')
	# Zhen form:
	zhen = BYHK()	# from games.py
	a_star_game(Huarongdao(zhen), '比翼横空')
	print('finished 比翼横空')
	# Zhen form:
	zhen = QGWG()	# from games.py
	a_star_game(Huarongdao(zhen), '巧过五关')
	print('finished 巧过五关')
	# Zhen form:
	zhen = WJBG()	# from games.py
	a_star_game(Huarongdao(zhen), '五将逼宫')
	print('finished 五将逼宫')
	# Zhen form:
	zhen = BLCY()	# from games.py
	a_star_game(Huarongdao(zhen), '兵临曹营')
	print('finished 兵临曹营')
	# Zhen form:
	zhen = SJLG()	# from games.py
	a_star_game(Huarongdao(zhen), '四将连关')
	print('finished 四将连关')
	# Zhen form:
	zhen = XJZZC()	# from games.py
	a_star_game(Huarongdao(zhen), '新近在咫尺')
	print('finished 新近在咫尺')
	# Zhen form:
	zhen = XLQB()	# from games.py
	a_star_game(Huarongdao(zhen), '星罗棋布')
	print('finished 星罗棋布')
	# Zhen form:
	zhen = SMBF()	# from games.py
	a_star_game(Huarongdao(zhen), '四面八方')
	print('finished 四面八方')
	# Zhen form:
	zhen = NQCT()	# from games.py
	a_star_game(Huarongdao(zhen), '牛气冲天')
	print('finished 牛气冲天')
	# Zhen form:
	zhen = DBQJ()	# from games.py
	a_star_game(Huarongdao(zhen), '调兵谴将')
	print('finished 调兵谴将')
	# Zhen form:
	zhen = BSZL()	# from games.py
	a_star_game(Huarongdao(zhen), '背水列阵')
	print('finished 背水列阵')
	# Zhen form:
	zhen = HDLM2()	# from games.py
	a_star_game(Huarongdao(zhen), '横刀立马2')
	print('finished 横刀立马2')
	'''
	print('finished all!')
	time_elapsed = time.time() - start_time
	print('total time took: ', time_elapsed)

if __name__ == '__main__':
	main()