#2 + 2 * 2, до тех пор пока не решит правильно

user_int1 = 0

while user_int1 != 6: 
    user_in = input("Решите уравнение 2 + 2 * 2. Введите решение: ")
    user_int1 = int(user_in)
    print("не то! пересчитать")
    
    #user_once_again = input("Решите уравнение 2 + 2 * 2. Введите решение: ")
    #user_int2 = int(user_once_again)

print("Конец")