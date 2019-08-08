# Задача
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
print("Наибольшее произведение-палиндром")

num = int(input("Введите число: "))

simpNum = 2
while num != 1:
    if num % simpNum == 0:
        print(str(num) + " | " + str(simpNum))
        num = num // simpNum
    else:
        simpNum += 1