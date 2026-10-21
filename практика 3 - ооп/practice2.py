class Transport:
    def __init__(self, name):
        self.name = name

    def description(self):
        return f"Транспорт - {self.name}"

class Car(Transport):
    def description(self):
        return f"Транспорт - {self.name}, тип коробки передач - {self.transmission}"
    def __init__(self, name, transmission):
        super().__init__(name)
        self.transmission = transmission

class Plane(Transport):
    def description(self):
        return f"Транспорт - {self.name}, размах крыльев - {self.wingspan}"
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wing_size = wingspan

class Bike(Transport):
    def description(self):
        return f"Транспорт - {self.name}, объем двигателя - {self.volume}"
    def __init__(self, name, volume):
        super().__init__(name)
        self.volume = volume


bike = Bike('Harley', '125cm^3')

print(bike.description())
