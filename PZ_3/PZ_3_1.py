#даны три целых числа: A, B, C. проверить истинность высказывания: "Ровно два из чисел A, B, C являются положительными".
a, b, c = input("введите первое число "), input("введите второе число "), input("введите третье число ")
#обработка исключений
while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print("неправильно ввели!")
        a = input("введите первое число ")
while type(b) != float:
    try:
        b = float(b)
    except ValueError:
        print("неправильно ввели!")
        b = input("введите второе число ")
while type(c) != float:
    try:
        c = float(c)
    except ValueError:
        print("неправильно ввели!")
        c = input("введите третье число ")
#проверка истинности
if (a>0 and b>0) or (a>0 and c>0) or (b>0 and c>0):
    print("высказывание истинно")
else:
    print("высказывание ложно")