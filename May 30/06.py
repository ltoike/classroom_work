user_in = input("Введите число: ")
number = int(user_in)

if number > 0:
    print ( "У Вас положительное число" )
elif number < 0:
    print ("У Вас отрицательное число")
elif number == 0:
    print ("Ваше число равно нулю")
else:
    print ("Ошибка")
print("Конец.")