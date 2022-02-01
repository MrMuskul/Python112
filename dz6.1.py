from random import randint
a = []
for i in range(20):
    x = randint(0, 100)
    a.append(x)
s = 0
for i in range(20):
    s += a[i]

print(s)