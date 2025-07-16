class akshu:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def ishan(self):
        print(f"my brand name is {self.brand} my model {self.model}")

class Vedant(akshu):
    def __init__(self, brand, model,colour):
        super().__init__(brand, model)
        self.colour = colour
        
# mycar = akshu("Toyota","Fortuner")
# print(mycar.brand)
# print(mycar.model)
# print(mycar.ishan())

car = Vedant("Toyota","Fortuner","Black")
print(car.brand)
print(car.model)
print(car.colour)




