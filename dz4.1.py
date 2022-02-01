n = int(input("Длинна списка: "))
a = []
for i in range(n):
    x = int(input())
    a.append(x)

print(a[::2])