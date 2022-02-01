n = int(input("Введите кол-во чисел последовательности: "))

max = 0
s = 0
x = float(input("Введите число: "))
s += x
max = x
min = x
for i in range(0, n-1):
    x = float(input("Введите число: "))
    if (x > max):
        max = x
    if (x < min):
        min = x
    s = s + x

print("Кол-во чисел", n)
print("Средне арифметическое", round(s/n, 1))
print("Минимальное число:", min)
print("Максимальное число:", max)