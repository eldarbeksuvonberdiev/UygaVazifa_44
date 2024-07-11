def file_yoz():
	print("Nechta foydalanuvchi kiritmoqchisiz: ")
	soni = int(input("Soni: "))
	print("Ma'lumotlar: Ism(Kim) Daraja(Middle) oylik(450) Bonus(100) bo'lim(1-Bo'lim) ")
	for i in range(soni):
		with open("It_programmers.txt","a") as f:
			f.write(input() + " " + "\n")
#file_yoz()

with open("It_programmers.txt", "r") as f:
	malumotlar = f.read()[:-1]
	malumotlar = malumotlar.split("\n")
for ind, malumot in enumerate(malumotlar):
	malumotlar[ind] = malumot.split(" ")[:-1]
	malumotlar[ind][3] = int(malumotlar[ind][3])
b1,b2,b3 = 0,0,0

for malumot in malumotlar:
	 _, _,  _, bonus, bolim = malumot
"""	print(bonus)
#	bolim = bolim.split("-")
	gurux,_ = bolim
	if gurux == 1:
		b1 += bonus
	elif gurux == 2:
		b2 += bonus
	else :
		b3 += bonus
"""
if b1 > b2 > b3:
	print("1 - bo'lim")
elif b2 > b1 > b3:
	print("2 bo'lim")
else:
	print("3 bo'lim")
