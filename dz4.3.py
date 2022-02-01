a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
k = 0
for j in range(len(a)):
    for i in range(len(a)):
        if (a[j] == a[i] and j != i):
            k += 1 
    if (k == 0):
        print(a[j], end=" ")
    k = 0
            