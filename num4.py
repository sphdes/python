#codeabbeyproblem4

probinput="""
-3468441 775013
-7306335 9006046
3804239 -1071517
7871041 9447092
-918097 7984929
2392230 7688506
7652971 3688464
-1285075 -7339946
-735056 7920395
8842813 -6667974
9144823 811849
5566392 1817160
-9282349 -8172768
2686446 6968454
-8704916 8844439
-7489536 -2173357
-380548 -4795871
-3167311 -6576308
4132611 -5296269
-7129216 -6785486
-7311340 5263014
-9096979 -9658369
-1048521 -382055
"""

basic = [int(elm) for elm in probinput.split()]
listAns = []

def prob4():
	while len(basic) != 0:
		set1 = basic.pop(0)
		set2 = basic.pop(0)
		if set1 < set2:
			listAns.append(set1)
		else:
			listAns.append(set2)
		

prob4()

listAns = ' '.join(map(str,listAns))

print listAns

