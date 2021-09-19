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