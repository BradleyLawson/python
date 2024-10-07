class Person: 
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
    # def __str__(self):
    #     return(f"")

person1 = Person("Brad", 45, "Male", "6'3", 250)

print(person1.__dict__)