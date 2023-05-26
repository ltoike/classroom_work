user_in1 = input("Введите первое число: ")
user_in2 = input("Введите второе число: ")

try:
    num1 = float(user_in1)
    num2 = float(user_in2)
    num3 += 1
except ValueError as my_error:
    print(my_error)
    message = "Вы ввели неправильные данные "
except NameError:
    message = "Нет такой переменной"
else:
    sum = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    message = template % (sum, sub, mul, div)

print(message)
