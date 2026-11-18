import unittest
from supplier import Supplier
from product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from order_line import OrderLine
from product_factory import ProductFactory


class TestProductValidation(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier("S001", "TechSource", "sales@techsource.com")

    def test_price_of_zero_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "Price must be greater than zero"):
            PhysicalProduct("P001", "Lamp", 0, 5, self.supplier, 1.0)

    def test_negative_price_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "Price must be greater than zero"):
            DigitalProduct("D001", "Editor", -10.0, 5, self.supplier, 100.0)

    def test_negative_stock_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "Stock quantity cannot be negative"):
            PhysicalProduct("P001", "Lamp", 10.0, -1, self.supplier, 1.0)

    def test_zero_stock_is_allowed(self) -> None:
        product = PhysicalProduct("P001", "Lamp", 10.0, 0, self.supplier, 1.0)
        self.assertEqual(product.get_stock(), 0)

    def test_update_stock_rejects_negative_values(self) -> None:
        product = PhysicalProduct("P001", "Lamp", 10.0, 5, self.supplier, 1.0)
        with self.assertRaises(ValueError):
            product.update_stock(-3)
        self.assertEqual(product.get_stock(), 5)

    def test_digital_product_cannot_skip_the_stock_rule(self) -> None:
        product = DigitalProduct("D001", "Editor", 10.0, 5, self.supplier, 100.0)
        with self.assertRaises(ValueError):
            product.update_stock(-1)

    def test_factory_passes_validation_through(self) -> None:
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P001", "Lamp", -1.0, 5, self.supplier)

    def test_valid_update_stock_works_on_every_product_type(self) -> None:
        products: list[Product] = [
            PhysicalProduct("P001", "Lamp", 10.0, 5, self.supplier, 1.0),
            DigitalProduct("D001", "Editor", 10.0, 5, self.supplier, 100.0),
        ]
        for product in products:
            product.update_stock(12)
            self.assertEqual(product.get_stock(), 12)


class TestOrderLineValidation(unittest.TestCase):
    def setUp(self) -> None:
        supplier = Supplier("S001", "TechSource", "sales@techsource.com")
        self.product = PhysicalProduct("P001", "Lamp", 10.0, 5, supplier, 1.0)

    def test_quantity_of_zero_is_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "Quantity must be greater than zero"):
            OrderLine(self.product, 0)

    def test_negative_quantity_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            OrderLine(self.product, -2)

    def test_valid_quantity_is_accepted(self) -> None:
        line = OrderLine(self.product, 3)
        self.assertAlmostEqual(line.calculate_subtotal(), 30.0)


if __name__ == "__main__":
    unittest.main()
