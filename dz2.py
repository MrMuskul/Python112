n = int(input("Количество символов: "))
sign = input("Тип символа: ")
print("0 - горизонтальная")
print("1 - вертикальная")
i = int(input("Ориентация линии: "))

if (i == 0):
    print((sign+" ")*n)
else:
    while(n > 0):
        print(sign)
        n -= 1
    
