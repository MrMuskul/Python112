a = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
f = 0

for f in a:
    for j in f:
        print(j, end="\t")
    print()

print()
k = 0

for j in f:
    for f in a:
        print(f[k], end="\t")
    print()
    k+=1