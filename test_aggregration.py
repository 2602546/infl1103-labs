from supplier import Supplier
from PhysicalProduct import PhysicalProduct
from inventory import Inventory

supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
guitar = PhysicalProduct("P001", "Guitar", 499.00, 5, supplier, 3.5)

inventory_a = Inventory()
inventory_b = Inventory()

print("PREDICT FIRST: after the Product is removed from Inventory A,")
print("will the Product still work? Why?")
input("Write your prediction down, then press Enter to run the test: ")