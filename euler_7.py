# Задача
# Какое число является 10001-ым простым числом?

print("10001-ое простое число")

currNum = 1 # Номер текущего числа
number = 2  # Начальное число

while currNum <= 10001:
    for i in range(number):
        if number % (i + 1) == 0 and i + 1 != 1 and number / (i + 1) != 1.0:
            break
        if number / (i + 1) == 1.0:
            currNum += 1
    number += 1
print(number)