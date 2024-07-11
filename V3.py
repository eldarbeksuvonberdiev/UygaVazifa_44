def file_yoz():
	print("Nechta foydalanuvchi kiritmoqchisiz: ")
	soni = int(input("Soni: "))
	print("Ma'lumotlar: Ism(Kim) Daraja(Middle) oylik(450) Bonus(100) bo'lim(1-Bo'lim) ")
	for i in range(soni):
		with open("It_programmers.txt","a") as f:
			f.write(input() + " " + "\n")
file_yoz()

with open("It_programmers.txt", "r") as f:
	malumotlar = f.read()
	malumotlar = malumotlar.split()
print(malumotlar)
