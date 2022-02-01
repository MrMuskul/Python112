a = 1
b = 2

(a, b) = (b, a)

print(a, b)

name = input("What is your name? ")
ages = input("How old are you? ")
city = input("Where are you living? ")

print("This is", name)
print("He is", ages)
print("He lives in", city)

print("Решите пример: 4 * 100 - 54")
ans = int(input("Ваш ответ: "))
print("Правильный ответ: 346")
print("Ваш ответ:", ans)

n = int(input("Введите пятизначное число: "))

ans = (n//10000) * (n//1000%10) * (n//100%10) * (n//10%10) * (n%10)
avg = ((n//10000) + (n//1000%10) + (n//100%10) + (n//10%10) + (n%10)) / 5
print("Произведение цифр числа " + str(n) + ": " + str(ans))
print("Среднее арифметическое:", avg)