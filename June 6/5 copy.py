import random

def get_random_int(min, max):
    result = random.random() * (max-min)
    final_result = result + min
    return int(final_result)

def game(my_random, min, max):
    user_in = input("Угадай число от %s до %s:" %(min, max))
    try:
        user_num = int(user_in)
    except ValueError:
        print("Только целое число!")
        game(my_random, min, max)
    else:
        if my_random > user_num:
            print("Больше")
            game(my_random, min, max)
        elif my_random < user_num:
            print("Меньше")
            game(my_random, min, max)
        else:
            print("Поздравляем, %d!" % my_random)
            print("Конец!")

my_random = get_random_int(0, 20)
game(my_random, 0, 20)