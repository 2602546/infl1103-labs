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

order1 = Order("O001")
order1.add_order_line(guitar, 2)
order1.add_order_line(antivirus, 1)

order2 = Order("O002")
order2.add_order_line(guitar, 1)

print()
order1.display_order()
print()
order2.display_order()

line_a = order1.get_order_lines()[0]
line_b = order2.get_order_lines()[0]
print("\nOrderLine objects created:", len(order1.get_order_lines()) + len(order2.get_order_lines()))
print("The two Guitar OrderLines are the same object:", line_a is line_b)
print("The two Guitar OrderLines refer to the same Product:", line_a.get_product() is line_b.get_product())
print("Order 1 id:", id(line_a), "| Order 2 id:", id(line_b), "| Product id:", id(guitar))

print("\nRemoving the Antivirus line from Order O001:")
order1.remove_order_line("D001")
order1.display_order()
print("Antivirus Product still exists:", antivirus.get_name())