

lim = int(input("List qiymatlar sonini kiriting: "))
lst = []
soniya = lim * 2
for i in range(lim):
	lst.append(input(f"{i + 1} - qiymat: "))

for i in range(0,lim - 1):
	if lst[i].lower() != lst[i + 1].lower():
		soniya += 1
print(soniya)
