from supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from order import Order

supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
guitar = PhysicalProduct("P001", "Guitar", 499.00, 5, supplier, 3.5)
antivirus = DigitalProduct("D001", "Antivirus", 29.90, 100, supplier, 250.0)

print("PREDICT FIRST: if the same Product is added to two different Orders,")
print("how many OrderLine objects and how many Product objects will exist?")
input("Write your prediction down, then press Enter to run the test: ")