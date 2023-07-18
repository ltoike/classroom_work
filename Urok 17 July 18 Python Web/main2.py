class House:
    def __init__(self, floors, color, rooms, bathrooms):
        self.floors = floors
        self.color = color
        self.rooms = rooms
        self.bathrooms = bathrooms
    def get_info(self):
        info = "Дом %d - этажный, цвета %s, комнаты: %d, ванных комнат: %d" % \
               (self.floors, self.color, self.rooms, self.bathrooms)
        return info
    def change_color(self, new_color):
        if new_color:
            self.__color = new_color
#my_house = HouseWithBalcony(2, "красный", 6, 2, 2)
#print(my_house.get_info())

class HouseWithBalcony(House): #принцип наследования
    def __init__(self, floors, color, rooms, bathrooms, balconys):
        super().__init__(floors, color, rooms, bathrooms)
        self.balconys = balconys
    def get_info(self):
        info = super().get_info()
        return info + f", балконов: {self.balconys}"
my_house = HouseWithBalcony(2, "красный", 6, 2, 2)
my_house.change_color("зеленый")
info = my_house.get_info()
print(info)


