'''Restaurant Menu Management: Develop a program for a restaurant to manage its menu items. 
It should allow adding, removing, and updating menu items with details like name, price, 
description, and category (e.g., appetizer, main course, dessert). The program should also 
display the complete menu and filter items based on category.'''

menu = {"appetizer": [], 
        "main course": [], 
        "dessert": []}

while True:
    def add():
        name = input("Enter the name of the item: ")
        price = int(input("Enter the price of the item: "))
        category = input("Enter the category of the item (appetizer/main course/dessert): ")
        description = input("Enter the description of the item: ")

        if category in menu:
            menu[category].append({"name": name, "price": price, "description": description})
        else:
            print("Invalid category. Please choose from 'appetizer', 'main course', or 'dessert'.")

    add()
    def remove_item(name):
        for category in menu:
            for item in menu[category]:
                if item["name"] == name:
                    menu[category].remove(item)
                    print("Item removed successfully.")
                    return
        print("Item not found.")


    user_Input = input("Do you want to add or remove  items: add/remove/quit/menu ")
    if user_Input == "remove":
        rev = input("Enter the name of item to remove: ")
        remove_item(rev)
        print(menu)
    elif user_Input == "menu":
        print(menu)
    elif user_Input == "quit":
        break
print(menu)