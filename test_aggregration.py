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

inventory_a.add_product(guitar)
print("\nIn Inventory A:", inventory_a.find_product("P001") is guitar)

removed = inventory_a.remove_product("P001")
print("Removed from Inventory A:", removed)
print("Still in Inventory A:", inventory_a.find_product("P001") is not None)