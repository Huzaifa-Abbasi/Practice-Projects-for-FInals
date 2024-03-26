'''Develop a program to simulate a basic online shop for selling products. It 
should display a list of available products with details like name, price, and quantity. The 
program should allow users to add items to their cart, view cart contents, and calculate the total 
cost'''

products = {
    "Laptop": {"price": 1000, "quantity": 10},
    "Headphones": {"price": 100, "quantity": 20},
    "Mouse": {"price": 20, "quantity": 50},
    "Keyboard": {"price": 50, "quantity": 30}
}


cart = []

def add_to_cart():
    name_of_product = input("Enter the name of product: ")
    if name_of_product in products:
        quantity_of_products = int(input("Enter the quantity of products: "))
        if products[name_of_product]["quantity"] >= quantity_of_products:
            products[name_of_product]["quantity"] -= quantity_of_products
            cart.append(products[name_of_product])
            cart[-1]["quantity"] = quantity_of_products
            total = products[name_of_product]["price"] * quantity_of_products


            print(f"{quantity_of_products} {name_of_product} added to the cart. and total amount is {total}")
        else:
            print(f"Only {products[name_of_product]['quantity']} {name_of_product} available in the shop.")
    else:
        print("No product found by the name.")

add_to_cart()
print(cart)