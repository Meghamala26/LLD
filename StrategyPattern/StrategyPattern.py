# when 2 or more child of a parent class have same functionality, 
# to avoid duplication, 
# separate the functionality as an interface that can be injected in the parent class constructor.

from abc import ABC, abstractmethod

class DriveStrategy(ABC):
    @abstractmethod
    def drive(self):
        pass
class SportDriveStrategy(DriveStrategy):
    def drive(self):
        print(f"Sport drive mode.")
class NormalDriveStrategy(DriveStrategy):
    def drive(self):
        print(f"Normal drive mode.")

class Vehicle():
    def __init__(self,driveStrategy:DriveStrategy):
        self._driveStrategy = driveStrategy
    def drive(self):
        self._driveStrategy.drive()

class SportVehicle(Vehicle):
    def __init__(driveStrategy:DriveStrategy):
        super().__init__(SportDriveStrategy())

class RegularVehicle(Vehicle):
    def __init__(driveStrategy:DriveStrategy):
       super().__init__(NormalDriveStrategy())

if __name__ == "__main__":
    sportVehicle = SportVehicle()
    regularVehicle = RegularVehicle()
    sportVehicle.drive()
    regularVehicle.drive()