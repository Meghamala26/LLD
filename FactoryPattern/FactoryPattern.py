#when we need to create different class objects based on scenario(input string in Factory class)
# abstract Factory pattern -> Factory of factories, 
# basically there are 2 or more types of factory pattern sub classes grouping different shape classes, 
# and another factory class 2 creates objects of factory pattern sub class based on scenario.
from abc import ABC, abstractmethod

#abstract class Shape
class Shape(ABC):
    @abstractmethod
    def getShape(self):
        pass

class Circle(Shape):
    def getShape(self):
        return "Circle"
class Rectangle(Shape):
    def getShape(self):
        return "Rectangle"
    
class ShapePattern:
    @staticmethod
    def displayShape(shape: str):
        if shape == "circle":
            return Circle()
        elif shape == "rectangle":
            return Rectangle()
        else:
            raise ValueError(f"Unknown shape type {shape}")
        
if __name__ == "__main__":
        shapePatternObj = ShapePattern()
        shape1 = shapePatternObj.displayShape("circle")
        print(shape1.getShape())
        


