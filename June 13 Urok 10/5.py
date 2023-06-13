class Kettle():
    material = ""
    color = ""
    volume = 0
    water = 0

    def __init__(self, material, color, volume):
        self.material = material
        self.volume = volume
        self.color = color
        
    def fill(self, liters):
        self.water += liters
        print(f"Теперь в чайнике {self.water} л")

my_kettle = Kettle("bamboo", "red", 5)
my_kettle.fill(3)

Kettle.color = "black"
print(my_kettle.color)