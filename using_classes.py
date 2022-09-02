class Car:
    def __init__(self, type):
        self.type = type
        self.message = "Eu sou un carro do tipo: "+type


car = Car("Ferrari")

print(car.message)
