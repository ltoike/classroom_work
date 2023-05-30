user_in = input("Ваш возраст? ")

try:
    user_age = int(user_in)
except ValueError:
    user_age = " "
if type(user_age) is int:
    if 0 < user_age < 120:
        message = "Ваш возраст похож на реальный"
    else: 
        message = "Врешь"
else:
    message = "Вы ввели не число"

print(message)


'''        
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
'''