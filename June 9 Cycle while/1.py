num = 1

if num < 10:
    print("меньше")
else:
    print("больше или равно")

while num < 10: #до тех пор пока (повторяется); else не обязательно. Бесконеч - 1 и True. break внутри функция помогает выйти
    num += 1
    if num == 5:
        continue #способ пропустить - continue
    print("меньше", num)
else:
    print("больше или равно")

print("Конец")