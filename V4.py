def xona_yig(x):
	sum = 0
	while x > 0:
		sum += x % 10
		x //= 10
	return sum

def my_sort(lst: list) -> list:
	lst.sort(key = xona_yig)
	return lst

lim = int(input("List qiymatlari sonini kiriting: "))
lst = []
for i in range(lim):
	while True:
		son = int(input(f"{i + 1} - Qiymat: "))
		try:
			if son >= 0:
				lst.append(son)
				break
			else:
				raise ValueError("Manfiy son kiritish mumkin emas!")
		except ValueError as ve:
			print(f"ValueError: {ve}")
sorted = my_sort(lst)
print(sorted)
