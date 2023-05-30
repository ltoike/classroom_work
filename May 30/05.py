user_in = input("Введите стоимость покупки: ")
cost = float(user_in)

if cost < 1000:
    print ( "Скидок нет" )
elif cost < 2000:
    print ("Скидка 2%")
elif cost < 5000:
    print ("Скидка 5%")
else:
    print ("Скидка 10%")
print("Конец.")

'''
cost = 1500
if cost < 1000:
    print ( "Скидок нет" )
if cost < 2000:
    print ("Скидка 2%")
if cost < 5000:
    print ("Скидка 5%")
else:
    print ("Скидка 10%")
print("Конец.")
'''