first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8, 9, 10]

first_list.append(6)
print(first_list)

first_list.extend(second_list)
print(first_list)

first_list.insert(4, "sgs")
print(first_list)
####
third_list = [2, 5, 5, True, "CAKE", "olol"]
element_removed = third_list.remove("CAKE")
print(third_list, element_removed)

element_popped = third_list.pop(3)
print(third_list, element_popped)

third_list.clear()
print(third_list)

####

first_list = [1, 2, 4, 4, True, "cake", "fs"]
my_index = first_list.index("fs")
print(my_index)

index_two = first_list.count(4)
print(index_two)
###
word_list = ["cake", "fs", "gregory", "ivory", "bee"]
sort = word_list.sort()
print(word_list)
###
word_list = ["gregory", "ivory", "bee", 542737, 22]
reverse = word_list.reverse()
print(word_list)

other_list = word_list.copy()
other_list[2] = "welcome"
print(other_list)
print(other_list is word_list)
print(word_list)


class Dog:
    type = ""
    size = 0
    color = ""
    def __init__(self, type, size, color):
        self.type = type
        self.size = size
        self.color = color
    def bark(self):
        print("Owf")
        print(self.color)
    my_little_dog = Dog("foxterier", 28, "white")
    my_little_dog.bark()