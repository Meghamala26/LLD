from abc import ABC, abstractmethod

class StockObserver(ABC):
    @abstractmethod
    def update(self):
        pass

class StocksObservable(ABC):
    @abstractmethod
    def add(self, observer: StockObserver):
        pass
    @abstractmethod
    def remove(self, observer: StockObserver):
        pass
    @abstractmethod
    def notify(self):
        pass
    @abstractmethod
    def setStockCount(self, stockAmount:int):
        pass
    @abstractmethod
    def getStockAmount(self):
        pass
    @abstractmethod
    def getType(self):
        pass

class EmailNotificationService(StockObserver):
    def __init__(self, emailId: str, stockObservable: StocksObservable):
        self._emailId = emailId
        self._stockObservable = stockObservable
    
    def update(self):
        self.sendMail()
    
    def sendMail(self):
        print(f"{self._stockObservable.getType()} has been restocked. New stock: {self._stockObservable.getStockAmount()}")


class IphoneObservable(StocksObservable):
    def __init__(self):
        self._observers = []
        self._type = "iphone"
        self._stock = 0

    def add(self, observer: StockObserver):
        self._observers.append(observer)

    def remove(self, observer: StockObserver):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update()
   
    def setStockCount(self, stockAmount:int):
        if self._stock == 0:
            self._stock+=stockAmount
            self.notify()
        else:
            self._stock+=stockAmount


    def getStockAmount(self):
        return self._stock
    
    def getType(self):
       return self._type


if __name__ =="__main__":
    iphoneObservable = IphoneObservable()
    observer1 = EmailNotificationService("xyx@gmail.com", iphoneObservable)
    observer2 = EmailNotificationService("xyx@gmail.com", iphoneObservable)

    iphoneObservable.add(observer1)
    iphoneObservable.add(observer2)
    iphoneObservable.setStockCount(100)
    iphoneObservable.setStockCount(50)


    




    
