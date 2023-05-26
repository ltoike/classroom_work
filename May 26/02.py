user_hours = input("Который час?  ")
user_minutes = input("Сколько минут?  ")
user_seconds = input("Сколько секунд?  ")
seconds_total = 24 * 60 * 60

try:
    hours = int(user_hours)
    minutes = int(user_minutes)
    seconds = int(user_seconds)
except ValueError:
    message = "Вы ввели не числа"
else:
    seconds_passed = hours * 60 * 60 + minutes * 60 + seconds
    seconds_left = seconds_total - seconds_passed
    message = "Осталось %s секунд" % seconds_left
    
print(message)