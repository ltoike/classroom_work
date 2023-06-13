import random

def get_random_int(min, max):
    result = random.random() * (max-min)
    final_result = result + 10
    return int(final_result)

num = get_random_int(10, 20)
print(num)