from supplier import Supplier
from PhysicalProduct import PhysicalProduct
from inventory import Inventory

supplier = Supplier("S001", "TechSource Pte Ltd", "sales@techsource.com")
guitar = PhysicalProduct("P001", "Guitar", 499.00, 5, supplier, 3.5)