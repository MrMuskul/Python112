n = int(input("Длинна списка: "))
a = []
for i in range(n):
    x = int(input())
    a.append(x)

for i in range(1, n):
    if (a[i] > a[i-1]):
        print(a[i], end=" ")