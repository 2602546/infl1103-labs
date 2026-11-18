import unittest
from supplier import Supplier
from product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from product_factory import ProductFactory


class TestProductFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier("S001", "TechSource", "sales@techsource.com")

    def test_creates_physical_product_with_weight(self) -> None:
        product = ProductFactory.create("physical", "P001", "Lamp", 25.0, 10, self.supplier, 2.5)
        self.assertIsInstance(product, PhysicalProduct)
        assert isinstance(product, PhysicalProduct)
        self.assertEqual(product.get_weight(), 2.5)

    def test_creates_digital_product_with_download_size(self) -> None:
        product = ProductFactory.create("digital", "D001", "Editor", 49.9, 100, self.supplier, 300.0)
        self.assertIsInstance(product, DigitalProduct)
        assert isinstance(product, DigitalProduct)
        self.assertEqual(product.get_download_size(), 300.0)

    def test_factory_returns_the_base_product_type(self) -> None:
        for product_type in ["physical", "digital"]:
            product = ProductFactory.create(product_type, "X001", "Item", 10.0, 1, self.supplier)
            self.assertIsInstance(product, Product)

    def test_extra_is_optional(self) -> None:
        product = ProductFactory.create("physical", "P001", "Lamp", 25.0, 10, self.supplier)
        self.assertIsInstance(product, PhysicalProduct)

    def test_unknown_product_type_raises_value_error_with_clear_message(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unknown product type: service"):
            ProductFactory.create("service", "S001", "Installation", 30.0, 5, self.supplier)


if __name__ == "__main__":
    unittest.main()
