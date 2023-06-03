from product import NonStockableProduct

class Store:
    def __init__(self):
        self.products = []
    
    def add_products(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
    
    def get_total_quantity(self):
        return int(sum([product.get_quantity() for product in self.products if not isinstance(product, NonStockableProduct)]))
    
    def get_all_products(self):
        return [product for product in self.products if product.is_active()]
    
    def order(self, shopping_list):
        total_price = 0
        for item in shopping_list:
            product, quantity = item
            if product in self.products and product.is_active():
                total_price += product.buy(quantity)
            else:
                raise Exception('Product not available for purchase')
        return total_price
        
    def get_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        raise Exception('Product not found')

