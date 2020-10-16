class RaceCar:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.seats = 2

    def drive(self):
        print("The car is on the road")

#Creating an object with a class: Instanciation
formula1 = RaceCar('Ferrari','abc','red')


print("****** INFORMATION *******")
print(f'BRAND : {formula1.brand}')
print(f'MODEL : {formula1.model}')
print(f'COLOR : {formula1.color}')
print(f'SEATS : {formula1.seats}')

