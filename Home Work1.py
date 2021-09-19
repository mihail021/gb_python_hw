print('Hello World')
a ='hello'
b ='world!'
print(f"{a},{b}")
num1 = int(input('Введите число - '))
num2 = int(input('Введите число - '))
print(f"Вы ввели числа {num1} и {num2}")
word = input("Enter any word:")
print(f"{word} - отличный выбор!")

time = int(input("Введите время в секундах -"))
hours = time // 60
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")

n = input("Введите положительное число -")
print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

num_init = int(input('Введите целое положительное число -'))
maximum = num_init % 10
num = num_init

while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit

    if digit == 9:
        break

    num //= 10
    print(num)

print(f"Наибольшая цифра в числе {num_init} равна {maximum}")

revenue = float(input("Введите значение выручки - "))
costs = float(input("Введите значение издержек - "))
result = revenue - costs  # прибль
if result > 0:
    print(f"Поздравляю! Ваша компания работает с прибылью {result} !")
    print(f"Рентабельность выручки - {result / revenue:.3f}")
    persons = int(input("Сколько счастливых целых сотрудников работает в вашей компании? - "))
    print(f"Прибыль на одного сотрудника - {result / persons:.3f}")
elif result < 0:
  print(f"Вы работаете с убытком-{- result}")
else:
  print(f"Ноль - это тоже хороший результат! Зато стабильно!")

while True:
      days = 1
      start_km = float(input('Начальный результат - '))
      last_km = float(input('Финальный результат - '))
      if start_km <= 0 or last_km < 0:
          print('Результаты должны быть больше нуля! Стартовое значение != 0')
      else:
          while start_km < last_km:
              start_km *= 1.1
              days += 1
          print(f'Спортсмен добьется результата за {days} дней')

import math
start_km = 2
last_km = 3
print(math.ceil(math.log(last_km / start_km, 1.1)) + 1)