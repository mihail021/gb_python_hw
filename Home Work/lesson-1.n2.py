time = int(input("Введите время в секундах -"))
hours = time // 60
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f"{hours:02}:{minutes:02}:{seconds:02}")
