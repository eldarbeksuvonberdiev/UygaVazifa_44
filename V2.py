lim = int(input("Foydalanuvhilar sonini kiriting: "))
mydict = {}
ismlar = []
for i in  range(lim):
	ismi = input("Ismini kiriting: ")
	ismlar.append(ismi)
	mydict[ismi] = int(input("1 yoki 0 kiriting: "))
sanoq1 = 0
sanoq2 = 0

for ism in ismlar:
	if mydict.get(ism) == 1:
		sanoq1 += 1
	elif mydict.get(ism) == 0:
		sanoq2 += 1

if sanoq1 > sanoq2:
	print("1")
	for ism in ismlar:
		if mydict.get(ism) == 1:
			print(ism, end = " ")
elif sanoq1 < sanoq2:
	print("0")
	for ism in ismlar:
		if mydict.get(ism) == 0:
			print(ism, end = " ")
else:
	print("0")
	for ism in ismlar:
		if mydict.get(ism) == 0:
			print(ism, end = " ")

	print("\n1")
	for ism in ismlar:
		if mydict.get(ism) == 1:
			print(ism, end = " ")
