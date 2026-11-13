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