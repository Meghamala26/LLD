#Decorator pattern where there is a base class and 
# you can build more features(decorate) over the base class to create child class 
# and decorate over child class to add on more features.
#Decorate class has "IS-A" and "HAS-A" relationship with base class.
#Example : Pizza with add on toppings
from abc import ABC, abstractmethod

class BasePizza(ABC):
    @abstractmethod
    def cost(self):
        pass
class Margherita(BasePizza):
    def cost(self):
        return 100
class VegDelight(BasePizza):
    def cost(self):
        return 110
    
class PizzaDecorator(BasePizza):
    @abstractmethod
    def cost(self):
        pass
class ExtraCheeseTopping(PizzaDecorator):
    def __init__(self, basePizza : BasePizza):
        self._basePizza = basePizza
    def cost(self):
        return self._basePizza.cost() + 10
class MushroomTopping(PizzaDecorator):
    def __init__(self, basePizza):
        self._basePizza = basePizza
    def cost(self):
        return self._basePizza.cost() + 20
    
if __name__ == "__main__":
    print(f"Cost of mushroom extra cheese pizza = {MushroomTopping(ExtraCheeseTopping(Margherita())).cost()}")



