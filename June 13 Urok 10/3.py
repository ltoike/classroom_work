class Kettle():
    material = "steel"
    color = "red"
    volume = 2.4
my_kettle = Kettle() #1ая переменная 
other_kettle = Kettle() #2ая переменная 

Kettle.color = "white" #класс

my_kettle.color = "blue" #перем
print(my_kettle.color, other_kettle.color)
