import json
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from SubscriptionProduct import SubscriptionProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from supplier import Supplier


def create_product(d: dict, suppliers: dict[str, Supplier]) -> Product | None:
    supplier = suppliers.get(d.get("supplier_id", ""))
    if supplier is None:
        return None
    if d.get("type") == "physical":
        return PhysicalProduct(d["id"], d["name"], d["price"], d["stock"], supplier, d["weight"])
    elif d.get("type") == "digital":
        return DigitalProduct(d["id"], d["name"], d["price"], d["stock"], supplier, d["download_size"])
    return None


def load_inventory(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
    try:
        file = open("inventory.json", "r")
        data = json.load(file)
        file.close()
        for s in data["suppliers"]:
            suppliers[s["id"]] = Supplier(s["id"], s["name"], s["contact_email"])
        for d in data["products"]:
            product = create_product(d, suppliers)
            if product is not None:
                inventory.add_product(product)
        print("inventory.json found.")
        print("Inventory loaded successfully.")
    except FileNotFoundError:
        print("inventory.json not found. Starting with empty inventory.")
    except (KeyError, TypeError, ValueError):
        print("inventory.json could not be read. Starting with empty inventory.")


def save_inventory(inventory: Inventory, suppliers: dict[str, Supplier]) -> None:
    print("Saving inventory...")
    data = {
        "suppliers": [s.to_dict() for s in suppliers.values()],
        "products": [p.to_dict() for p in inventory.get_products()]
    }
    file = open("inventory.json", "w")
    json.dump(data, file, indent=2)
    file.close()
    print("Inventory saved successfully to inventory.json.")


def choose_supplier(suppliers: dict[str, Supplier]) -> Supplier:
    supplier_id = input("Supplier ID: ")
    if supplier_id in suppliers:
        print("Existing supplier selected.")
        return suppliers[supplier_id]
    name = input("Supplier Name: ")
    email = input("Supplier Email: ")
    supplier = Supplier(supplier_id, name, email)
    suppliers[supplier_id] = supplier
    print("New supplier created.")
    return supplier


def add_product(inventory):
    print("Add New Product")
    print("1. Physical Product")
    print("2. Digital Product")
    print("3. Subscription Product")
    choice = input("Product Type: ")
    if choice != "1" and choice != "2" and choice != "3":
        print("Invalid product type.")
        return
    pid = input("Product ID: ")
    name = input("Product Name: ")
    price = float(input("Price: "))
    stock = int(input("Stock Quantity: "))
    if choice == "1":
        weight = float(input("Weight (kg): "))
        product = PhysicalProduct(pid, name, price, stock, weight)
    elif choice == "2":
        download_size = float(input("Download Size (MB): "))
        product = DigitalProduct(pid, name, price, stock, download_size)
    else:
        duration = int(input("Duration (months): "))
        product = SubscriptionProduct(pid, name, price, stock, duration)
    inventory.add_product(product)
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
        product.display_information()
        print("Fulfilment:", product.get_fulfilment_info())
        if isinstance(product, CanBeShipped):
            print("Shipping Cost: $%.2f" % product.calculate_shipping_cost())
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