# Задача
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
print("Четные числа Фибоначчи")

fLine = True

prev = 0
curr = 0
fut  = 0
total = 0

while fut < 4000000:
    if fLine == True:
        prev = 1
        curr = 2
        fut = prev + curr

        total += 2
        fLine = False
    else:
        prev = curr
        curr = fut
        fut = prev + curr

        if fut % 2 == 0 and fut < 4000000:
            total += fut

print("Сумма: " + str(total))