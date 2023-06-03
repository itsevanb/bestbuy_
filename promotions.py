from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class PercentDiscount(Promotion):
    def __init__(self, discount):
        super().__init__('PercentDiscount')
        self.discount = discount

    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.discount / 100)
        
class SecondItemHalfPrice(Promotion):
    def __init__(self):
        super().__init__('SecondItemHalfPrice')

    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return full_price_items * product.price + half_price_items * product.price * 0.5
        
class BuyTwoGetOneFree(Promotion):
    def __init__(self):
        super().__init__('BuyTwoGetOneFree')

    def apply_promotion(self, product, quantity):
        group_of_three = quantity // 3
        remaining_items = quantity % 3
        return (group_of_three * 2 + remaining_items) * product.price