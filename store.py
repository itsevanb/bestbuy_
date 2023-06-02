from product import Product

class Store:
    def __init__(self):
        self.products = []
    
    def add_products(self, product):
        self.products.append(product)

    def remove_product(self, product):
         if product in self.products:
             self.products.remove(product)
    
    def get_total_quantity(self):
        return int(sum([product.get_quantity() for product in self.products]))
    
    def get_all_products(self):
        return [product for product in self.products if product.is_active()]
    
    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if product in self.products and product.is_active():
                total_price += product.buy(quantity)
            else:
                raise Exception('Product is not available for purchase')
        return total_price
        
    def get_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        raise Exception('Product not found')

def main():
    products = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

    store = Store()
    for product in products:
        store.add_products(product)
        
    active_products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(active_products[0], 1), (active_products[1], 2)]))

if __name__ == "__main__":
    main()