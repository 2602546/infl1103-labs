from supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

print("PREDICT FIRST: if you del supplier after creating the products,")
print("can each Product still display its supplier information?")
input("Write your prediction down, then press Enter to run the test: ")

supplier: Supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
guitar = PhysicalProduct("P001", "Guitar", 499.00, 5, supplier, 3.5)
antivirus = DigitalProduct("D001", "Antivirus", 29.90, 100, supplier, 250.0)

print("\nSupplier shown through each product:")
guitar.get_supplier().display_information()
antivirus.get_supplier().display_information()
print("Both products share one Supplier object:", guitar.get_supplier() is antivirus.get_supplier())

del supplier
print("\nAfter del supplier:")
guitar.get_supplier().display_information()
antivirus.get_supplier().display_information()
