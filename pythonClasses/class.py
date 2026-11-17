class Animal:
    pass

class Dog(Animal):  #dog inherits from the animal 
    pass

bruno = Dog()

print(type(bruno) == Animal)  #strict check       #false [because bruno is specifially a dog]
print(isinstance(bruno, Animal)) # Flexible check    #True [ works because dog is a type of animal ]


#Why You Should Always Use isinstance(
# type(x) == int is overly strict. If someone passes a custom number or a bool into your function, your code will reject it and break.
# isinstance(x, int) is smarter. It accepts standard integers and anything that behaves like an integer through inheritance.
# Bonus perk: isinstance() lets you check multiple types at once cleanly, like isinstance(x, (int, float)).