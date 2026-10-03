#Дано трёхзначное число. Найти сумму и произведение его цифр.
d = int(input("введите трёхзначное число"))
if d in rande(-999, 999):
    a = (d // 100)
    b = (d % 10)
    c = (d % 100 // 10)
    summa = (a + b + c)
    proizvedenie = (a * b * c)
    print("сумма цифер ", summa)
    print("произведение цифр ", proizvedenie)
else:
    Print("Ошибка: число не трёхзначно")