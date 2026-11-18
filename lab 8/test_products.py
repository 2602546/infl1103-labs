from product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from can_be_shipped import CanBeShipped

guitar = PhysicalProduct("P001", "Guitar", 499.00, 5, 3.5)
book = PhysicalProduct("P002", "Textbook", 60.00, 20, 1.0)
anvil = PhysicalProduct("P003", "Anvil", 150.00, 2, 50.0)
antivirus = DigitalProduct("D001", "Antivirus", 29.90, 100, 250.0)

guitar.display_information()
print(guitar.get_fulfilment_info())
antivirus.display_information()
print(antivirus.get_fulfilment_info())

for p in [guitar, book, anvil]:
    print("%s shipping cost: $%.2f" % (p.get_name(), p.calculate_shipping_cost()))

print("Digital can be shipped:", isinstance(antivirus, CanBeShipped))

try:
    generic = Product("X001", "Generic", 10.00, 1)
except TypeError as error:
    print("Cannot create Product directly:", error)
