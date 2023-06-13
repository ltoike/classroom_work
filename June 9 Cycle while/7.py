user_in = input("Введите число: ")
user_int = int(user_in)

for i in range(1,100):
    if i % user_int == 0:
        print(i)
