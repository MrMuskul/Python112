n = int(input("Введите количество элементов списка: "))
a = []

for i in range(n):
    x = int(input())
    a.append(x)

k = int(input("Введите индекс: "))

c = int(input("Введите значение: "))

a.insert(k, c)

print(a)