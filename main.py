from store import Store
from product import Product, NonStockableProduct, LimitedProduct

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250),
                 NonStockableProduct("Windows License", price=125),
                 LimitedProduct("Shipping", price=10, max_quantity=1)
               ]
best_buy = Store()
for product in product_list:
    best_buy.add_products(product)


def start(store):
    while True:
        print('Welcome to our store! Please select an option: ')
        print('1. List all products in store')
        print('2. Show total amount of products in store')
        print('3. Make an order')
        print('4. Exit')

        user_input = input('Enter your choice: ')

        if user_input == '1':
            products = store.get_all_products()
            for product in products:
                product.show()
        elif user_input == '2':
            total_quantity = store.get_total_quantity()
            print(f'Total quantity of products in store: {total_quantity}')
        elif user_input == '3':
            shopping_list = []
            while True:
                product_name = input('Enter product name: ')
                quantity = int(input('Enter quantity: '))
                product = store.get_product_by_name(product_name)
                shopping_list.append((product, quantity))
                if input('Do you want to add another product? (y/n): ') == 'n':
                    break
            try:
                total_price = store.order(shopping_list)
                print(f'Total price: ${total_price}')
            except Exception as e:
                print(e)
        elif user_input == '4':
            print('Thank you for shopping with us!')
            break
        else:
            print('Invalid option please try again')

if __name__ == "__main__":
    start(best_buy)