from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

guitar = PhysicalProduct("P001", "Guitar", 499.00, 5, 3.5)
antivirus = DigitalProduct("D001", "Antivirus", 29.90, 100, 250.0)

guitar.display_information()
antivirus.display_information()
