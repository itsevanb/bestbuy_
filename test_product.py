import pytest 
from product import Product

def test_create_product():
    #Creating a normal product works
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.is_active() == True

def test_invalid_product():
    #Creating a product with invalid details invokes an exception
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-1, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=1450, quantity=-1)

def test_inactive_product():
    #When product quantity is 0, it is inactive
    product = Product("MacBook Air M2", price=1450, quantity=100)
    product.set_quantity(0)
    assert product.is_active() == False

def test_buy_product():
    #Product purchase modifies the quantity and returns the right output
    product = Product("MacBook Air M2", price=1450, quantity=100)
    total_price = product.buy(10)
    assert product.quantity == 90
    assert total_price == 1450 * 10

def test_buy_too_much_product():
    #Buying more than the available quantity raises an exception
    product = Product("MacBook Air M2", price=1450, quantity=100)
    with pytest.raises(Exception):
        product.buy(101)

