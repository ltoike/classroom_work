class Kettle():
    temperature: 20
    material = ""
    color = ""
    volume = 0
    water = 0


    def __init__(self, material, color, volume):
        self.material = material
        self.color = color
        self.volume = volume
        
    def fill(self, liters):
        self.water += liters
        if self.water > self.volume:
            extra = self.water - self.volume
            print(f"Много воды. Вылилось! {self.water-self.volume} л")
            self.water = self.volume
        print(f"Теперь в чайнике {self.water} л")

    def pour(self, liters):
        if liters > self.water:
            print(f"Не могу вылить больше чем {self.water} л")
            self.water = 0
        else:
            self.water -= liters
        print(f"Теперь в чайнике {self.water} л")

    def boil(self):
        self.temperature = 100
        print("HOT")

my_kettle = Kettle("bamboo", "red", 5)
my_kettle.fill(7)
my_kettle.pour(7)
my.kettle.boil()


Kettle.color = "black"
print(my_kettle.color)
