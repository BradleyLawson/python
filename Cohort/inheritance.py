class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f'{self.color}, {self.year}, {self.make}, {self.color}'
    
car1 = Car("ford", "f150", 1998, "red")
print(car1)

class Ford(Car):
    def __init__(self, make, model, year, color, engine):
        super().__init__(make, model, year, color)
        self.engine = engine

    def __str__(self):
        return f'{self.color}, {self.year}, {self.make}, {self.color}, {self.engine}'
        
ford1 = Ford("Ford", "F150", "2018", "blue", "V8")
print(ford1)