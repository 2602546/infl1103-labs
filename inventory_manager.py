import json
from product import Product
from inventory import Inventory


def load_inventory(inventory):
    try:
        file = open("inventory.json", "r")
        data = json.load(file)
        file.close()
        for d in data:
            inventory.add_product(Product(d["id"], d["name"], d["price"], d["stock"]))
        print("inventory.json found.")
        print("Inventory loaded successfully.")
    except FileNotFoundError:
        print("inventory.json not found. Starting with empty inventory.")


def save_inventory(inventory):
    print("Saving inventory...")
    data = [p.to_dict() for p in inventory.get_products()]
    file = open("inventory.json", "w")
    json.dump(data, file)
    file.close()
    print("Inventory saved successfully to inventory.json.")


def add_product(inventory):
    print("Add New Product")
    pid = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    inventory.add_product(Product(pid, name, price, stock))
    print("Product added successfully!")


def update_stock(inventory):
    print("Update Stock")
    pid = input("Enter Product ID: ")
    product = inventory.search_product(pid)
    if product is None:
        print("Product not found.")
    else:
        print("Product Found:")
        print("Name:", product.get_name())
        print("Current Stock:", product.get_stock())
        new_stock = int(input("New Stock Quantity: "))
        product.update_stock(new_stock)
        print("Stock updated successfully!")


def search_product(inventory):
    print("Search Product")
    pid = input("Enter Product ID: ")
    product = inventory.search_product(pid)
    if product is None:
        print("Product not found.")
    else:
        print("Product Found")
        print("------------------------------------------------")
        print("ID:", product.get_product_id())
        print("Name:", product.get_name())
        print("Price: $%.2f" % product.get_price())
        print("Stock:", product.get_stock())
        print("------------------------------------------------")


print("========================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("========================================")

inventory = Inventory()
load_inventory(inventory)

while True:
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")
    option = input("Enter option: ")

    if option == "1":
        inventory.display_all()
    elif option == "2":
        add_product(inventory)
    elif option == "3":
        update_stock(inventory)
    elif option == "4":
        search_product(inventory)
    elif option == "5":
        save_inventory(inventory)
    elif option == "6":
        print("Saving inventory before exit...")
        save_inventory(inventory)
        print("Thank you for using Inventory Management System.")
        print("Program terminated.")
        break
    else:
        print("Invalid option.")