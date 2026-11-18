from supplier import Supplier
from product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from inventory import Inventory

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
guitar = PhysicalProduct("P001", "Guitar", 499.00, 5, supplier, 3.5)
antivirus = DigitalProduct("D001", "Antivirus", 29.90, 100, supplier, 250.0)

print("PREDICT FIRST: what will get_fulfilment_info() print for each product?")
input("Write your prediction down, then press Enter to run the test: ")

print("\nshow_product_details with each product type:")
show_product_details(guitar)
show_product_details(antivirus)

inventory = Inventory()
inventory.add_product(guitar)
inventory.add_product(antivirus)

print("\nOne loop over the Product collection:")
for product in inventory.get_products():
    product.display_information()
    print(product.get_fulfilment_info())

print("\nSame Product operation on every product (update_stock):")
for product in inventory.get_products():
    product.update_stock(10)
    print(product.get_name(), "stock is now", product.get_stock())

print("\nInventory operations still work:")
inventory.display_all_products()
