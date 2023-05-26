user_distance = input("Расстояние между двумя городами в км?  ")
user_time = input("За сколько часов вы хотите добраться?  ")

try:
    distance = int(user_distance)
    time = int(user_time)

except ValueError:
    message = "Вы ввели не числа"
else:
    desired_time = distance / time
    message = "Осталось %s секунд" % desired_time
    
print(message)