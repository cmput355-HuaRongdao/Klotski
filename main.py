# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan
from solver import *

def main():
	start_time = time.time()
	# Zhen form:
	zhen = TZYY()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('逃之夭夭')
	print('finished 逃之夭夭')
	# Zhen form:
	zhen = WHZJ()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('无横之局')
	print('finished 无横之局')
	# Zhen form:
	zhen = JDHL()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('将当后路')
	print('finished 将当后路')
	# Zhen form:
	zhen = QHHY()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('前呼后拥')
	print('finished 前呼后拥')
	# Zhen form:
	zhen = BYHK()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('比翼横空')
	print('finished 比翼横空')
	# Zhen form:
	zhen = QGWG()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('巧过五关')
	print('finished 巧过五关')
	# Zhen form:
	zhen = WJBG()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('五将逼宫')
	print('finished 五将逼宫')
	# Zhen form:
	zhen = BLCY()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('兵临曹营')
	print('finished 兵临曹营')
	# Zhen form:
	zhen = SJLG()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('四将连关')
	print('finished 四将连关')
	# Zhen form:
	zhen = XJZZC()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('新近在咫尺')
	print('finished 新近在咫尺')
	# Zhen form:
	zhen = XLQB()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('星罗棋布')
	print('finished 星罗棋布')
	# Zhen form:
	zhen = SMBF()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('四面八方')
	print('finished 四面八方')
	# Zhen form:
	zhen = NQCT()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('牛气冲天')
	print('finished 牛气冲天')
	# Zhen form:
	zhen = DBQJ()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('调兵谴将')
	print('finished 调兵谴将')
	# Zhen form:
	zhen = BSZL()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('背水列阵')
	print('finished 背水列阵')
	# Zhen form:
	zhen = HDLM2()	# from games.py
	Search_Solver(Huarongdao(zhen)).a_star_game('横刀立马2')
	print('finished 横刀立马2')
	print('finished all!')
	time_elapsed = time.time() - start_time
	print('total time took: ', time_elapsed)

if __name__ == '__main__':
	main()