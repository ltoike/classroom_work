user_money = input("Наберите трехзначное число ")

try:
    money = int(user_money)
    price = int(user_price)

except ValueError:
    message = "Вы ввели не числа"
else:
    your_change = money - price
    message = "Осталось %s денег" % your_change
    
print(message)