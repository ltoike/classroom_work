class Kettle():
    material = "steel"
    volume = 2.4
    color = "red"
    water = 0

    def fill(self, liters):
        self.water += liters
        print(f"Теперь в чайнике, {self.water} л")

my_kettle = Kettle()
other_kettle = Kettle()
my_kettle.color = "blue"
Kettle.color = "white"
print(my_kettle.color, other_kettle.color)

my_kettle.fill(2)
my_kettle.fill(1)
my_kettle.fill(1)
print(my_kettle.water)
