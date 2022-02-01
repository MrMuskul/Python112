from random import randint
f = False
k = 0
a = 1
num = randint(1, 100)
while (f != True):
    a = int(input("Введите число от 1 до 100: "))
    k += 1
    if(a == 0):
        print("Вы наигрались")
        break
    elif (a == num):
        print("Вы угадали заданное число с", k, "раза")
        break
    elif (a < num):
        print("Загаданное число больше")
    else:
        print("Загаданное число меньше")

        