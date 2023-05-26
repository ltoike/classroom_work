user_in1 = input("Введите первое число: ")
user_in2 = input("Введите второе число: ")

num1 = float(user_in1)
num2 = float(user_in2)

template = """
Сумма чисел:            %.2f
Разность чисел:         %.2f
Произведение чисел:     %.2f
Частное чисел:          %.2f
"""

sum = num1 + num2
sub = num1 - num 2
mul = num1 * num2
div = num1 / num2

message = template % (sum, sub, mul, div)

print(message)