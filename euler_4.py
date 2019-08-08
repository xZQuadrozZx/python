# Задача
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.
import math
print("Наибольшее произведение-палиндром")

def prime2(n):
	if int(math.sqrt(n)) == float(math.sqrt(n)):
		return(0)
	_sqr = round(math.sqrt(n))
	k = 0
	while a[k] < _sqr:
		if n % a[k] == 0 and a[k]!=1:
			return(0)
		k += 1
	if n!= 4 and n != 6 and n != 8:
		return(n)
	else:
		return(0)

a = [1]
i = 1
k = 0
n = 1
while True:
	i += n
	if prime2(i) != 0:
		a.append(i)
		k += 1
		#print('k= ' + str(k))
		if k == 10001:
			print(i)
			break