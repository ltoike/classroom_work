import random

def get_random_int(min, max):
    result = random.random() * (max-min)
    final_result = result + 10
    return int(final_result)

def game():
    user_in = input("Угадай число от 0 до 100: ")
    try:
        user_num = int(user_in)
    except ValueError:
        print("Только целое число!")
        game()
    else:
        if my_random > user_num:
            print("Больше")
            game()
        elif my_random < user_num:
            print("Меньше")
            game()
        else:
            print("Поздравляем, %d!" % my_random)
            print("Конец!")




my_random = get_random_int(0, 100)
game()