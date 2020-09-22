# Author: Shway Wang
# Date: 2020, September 15th
# Location: China Ningxia Yinchuan

from games import *
from heuristic import *
from a_star import *
import copy

def main():
	
	# Zhen form:
	zhen = TZYY()	# from games.py
	Heu_Solver(Huarongdao(zhen)).game('逃之夭夭')
	
	# Zhen form:
	zhen = WHZJ()	# from games.py
	Heu_Solver(Huarongdao(zhen)).game('无横之局')
	
	# Zhen form:
	zhen = JDHL()	# from games.py
	Heu_Solver(Huarongdao(zhen)).game('将当后路')
	
	# Zhen form:
	zhen = QHHY()	# from games.py
	Heu_Solver(Huarongdao(zhen)).game('前呼后拥')
	
	# Zhen form:
	zhen = BYHK()	# from games.py
	Heu_Solver(Huarongdao(zhen)).game('比翼横空')
	
	# Zhen form:
	zhen = QGWG()	# from games.py
	Heu_Solver(Huarongdao(zhen)).game('巧过五关')
	
	# Zhen form:
	zhen = WJBG()	# from games.py
	Heu_Solver(Huarongdao(zhen)).game('五将逼宫')
	# Zhen form:
	
	'''
	zhen = HDLM2()	# from games.py
	Heu_Solver(Huarongdao(zhen)).game('横刀立马')
	'''

if __name__ == '__main__':
	main()