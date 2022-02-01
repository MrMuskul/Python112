import imp
from random import randint
a = []
for i in range(10):
    x = randint(0, 100)
    a.append(x)
a.sort(reverse=True)
print(a)