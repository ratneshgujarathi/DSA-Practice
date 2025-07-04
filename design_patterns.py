# Singleton method
class Singleton:
    instance = None
    def __new__(cls):
        if not cls.instance:
            super().__new__(cls)
        return cls.instance
    

s1 = Singleton()
s2 = Singleton()


# Factory Pattern
class Car:
    def paint(self, color): pass

class Chevrolette(Car):
    def paint(self, color):
        print(f'Chevrolette car with color : {color}')
    
class Audi(Car):
    def paint(self, color):
        print(f'Audi car with color : {color}')
    

class CarFactory:
    @staticmethod
    def select_car(name):
        if name == 'Audi':
            return Audi()
        elif name == 'Chevrolette':
            return Chevrolette()
        else:
            raise Exception('Car name invalid')
        
car1 = CarFactory.select_car('Chevrolette')
car2 = CarFactory.select_car('Audi')
car1.paint('Black')
car2.paint('Red')


# Observor pattern
from abc import ABC, abstractmethod
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class NotificationService:
    observors = []

    def subscribe(self, *observers: Observer):
        for observer in observers:
            if not isinstance(observer, Observer):
                raise TypeError(f"{observer} is not a valid Observer")
            self.observors.append(observer)

    def notify(self, message):
        for observor in self.observors:
            observor.update(message)

class EmailNotifier(Observer):

    def update(self, message):
        print(f'Email Notification: {message}')


class SMSNotifier(Observer):

    def update(self, message):
        print(f'SMS Notification: {message}')

class WhatsappNotifier(Observer):

    def update(self, message):
        print(f'Whatsapp Notification: {message}')

    
NS = NotificationService()
NS.subscribe(EmailNotifier())
NS.subscribe(SMSNotifier(), WhatsappNotifier())

NS.notify("Order Id #3256 Shipped")


# Strategy Pattern
class DiscountStrategy:
    def apply(self, amount): pass

class NoDiscount(DiscountStrategy):
    def apply(self, amount): return amount

class TenPercentDiscount(DiscountStrategy):
    def apply(self, amount): return amount * 0.9

def checkout(amount, strategy: DiscountStrategy):
    return strategy.apply(amount)

print(checkout(50, TenPercentDiscount()))


