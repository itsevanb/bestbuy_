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
    
def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()

if __name__ == "__main__":
    main()