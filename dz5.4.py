n = int(input("Введите элементы списка: "))
a = []
for i in range(n):
    x = int(input())
    a.append(x)

ch = int(input("Введите число: "))

if ch in a:
    print("Число присутствует в элементах списка")
else:
    print("Число не присутствует в элементах списка")