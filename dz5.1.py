n = int(input("Введите длинну списка: "))
a = []
for i in range(n):
    x = int(input("Введите элемент списка: "))
    a.append(x)
ans = []
max = 0
for i in range(n):
    if (a[i] > 0):
        ans.append(a[i])
    if (a[i] > max):
        max = a[i]


print("Список: ", a)
print("Новый список из положительных элементов: ", ans)
print("Наибольший элемент списка: ", max)