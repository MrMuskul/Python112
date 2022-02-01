a = int(input("Введите размер поля: "))
b = int(input("Введите кол-во символов"))

if (a % 2 == 0):
    c = a
    a = round(a/2)
    for j in range(1, c+1):
        if (j % 2 != 0):
            for x in range(1, b+1):
                print(("*"*b+" "*b)*a)
        else:
            for x in range(1, b+1):
                print((" "*b+"*"*b)*a)
else:
    c = a
    a = round(a//2)
    for j in range(1, c+1):
        if (j % 2 != 0):
            for x in range(1, b+1):
                print(("*"*b+" "*b)*a, end="")
                print("*"*b)
        else:
            for x in range(1, b+1):
                print((" "*b+"*"*b)*a + " "*b)