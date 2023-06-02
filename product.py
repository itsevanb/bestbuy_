
class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise ValueError('Invalid product data')
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return float(self.quantity)
    
    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError('Invalid quantity')
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active
    
    def deactivate(self):
        self.active = False

    def show(self):
        print(f'{self.name} - ${self.price} - {self.quantity} left')

    def buy(self, quantity):
        if not self.active:
            print('Product is not available for purchase')
        if quantity > self.quantity:
            raise Exception('Not enough product in stock')
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity
    
class NonStockableProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=float('inf'))
    
    def show(self):
        print(f'{self.name} - ${self.price} - Non-stockable product')
    
    def buy(self, quantity):
        if quantity >1:
            raise Exception('Cannot buy more than 1')
        return self.price * quantity
    
class LimitedProduct(Product):
    def __init__(self, name,  price, max_quantity):
        super().__init__(name, price, quantity=max_quantity)
        
    def show(self):
        print(f'{self.name} - ${self.price} - Limited product, max quantity: {self.quantity}')

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception('Cannot buy more than max quantity')
        self.quantity -= quantity
        return self.price * quantity
    