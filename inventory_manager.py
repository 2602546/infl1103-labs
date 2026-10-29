from product import Product
from inventory import Inventory


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
inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
inventory.add_product(Product("P002", "Mouse", 25.50, 40))
inventory.add_product(Product("P003", "Keyboard", 45.00, 25))

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
        print("save_inventory() not implemented yet.")
    elif option == "6":
        print("Program terminated.")
        break
    else:
        print("Invalid option.")