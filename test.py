from util import *
# caoCao:
caoCao = CaoCao([1, 2])
# Jiangs:
zhaoYun = Jiang([3, 0], VER, 'y')
guanYu = Jiang([1, 0], HOR, 'g')
maChao = Jiang([0, 2], VER, 'm')
huangZhong = Jiang([3, 2], VER, 'h')
zhangFei = Jiang([0, 0], VER, 'z')
jiangList = [zhaoYun, guanYu, maChao, huangZhong, zhangFei]
# Bings:
b1 = Bing([1, 1])
b2 = Bing([2, 1])
b3 = Bing([0, 4])
b4 = Bing([3, 4])
bingList = [b1, b2, b3, b4]
zhen = Zhen(caoCao, jiangList, bingList)

savt = StateActionValueTable()
serialized = savt.serialize(zhen)
print(serialized)
z = savt.deserialize(serialized)
s = savt.serialize(z)
print(s)