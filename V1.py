lim = int(input("Listga nechta qiymat kiritmoqchisiz? "))
lst = []

for i in range(lim):
	lst.append(int(input(f"{i + 1}- qiymat: ")))
for i in range(lim - 1):
	if lst[i] > 0 and lst[i] == lst[i + 1] - 1:
		print(lst[i], lst[i + 1])
	elif lst[i] < 0 and lst[i] == lst[i + 1] + 1:
		print(lst[i], lst[i + 1])

