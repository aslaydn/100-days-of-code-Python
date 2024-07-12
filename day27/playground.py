def add(*args): # args:tuple
    sum = 0
    for n in args:
        sum+=n
    return sum

print(add(2,3,4))

def calculate(n,**kwargs): #kwargs:dictionary
    # for key,value in kwargs.items():
    #    print(key)
    #    print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3,multiply=5)    

class Car:
    def __init__(self,**kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")

my_car = Car(make="Nissan", model = "GT-R")
print(my_car.model)        