a = int(input("Введите число: "))
b = 0
c = 0
ans = a
while a > 0:
    b = a % 10
    c = c * 10 + b
    a = a // 10

if (c == ans):
    print("Число " + str(ans) + " - палиндром")
else:
    print("Число " + str(ans) + " - не палиндром")
    