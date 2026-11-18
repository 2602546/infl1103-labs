import inspect
import unittest
from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount


def make_order(discount: DiscountStrategy | None = None) -> Order:
    supplier = Supplier("S001", "TechSource", "sales@techsource.com")
    product = PhysicalProduct("P001", "Lamp", 50.00, 10, supplier, 1.0)
    order = Order("O001", discount)
    order.add_order_line(product, 5)
    return order


class TestDiscountStrategies(unittest.TestCase):
    def test_no_discount_returns_total_unchanged(self) -> None:
        self.assertEqual(NoDiscount().apply(250), 250)

    def test_percentage_discount_takes_percentage_off(self) -> None:
        self.assertAlmostEqual(PercentageDiscount(10).apply(250), 225)

    def test_bulk_discount_applies_at_or_above_threshold(self) -> None:
        self.assertAlmostEqual(BulkDiscount(200, 20).apply(250), 230)
        self.assertAlmostEqual(BulkDiscount(200, 20).apply(200), 180)

    def test_bulk_discount_does_not_apply_below_threshold(self) -> None:
        self.assertAlmostEqual(BulkDiscount(200, 20).apply(199), 199)

    def test_strategies_are_discount_strategies(self) -> None:
        for strategy in [NoDiscount(), PercentageDiscount(10), BulkDiscount(200, 20)]:
            self.assertIsInstance(strategy, DiscountStrategy)

    def test_discount_strategy_cannot_be_created_directly(self) -> None:
        with self.assertRaises(TypeError):
            DiscountStrategy()  # type: ignore[abstract]


class TestOrderUsesStrategy(unittest.TestCase):
    def test_order_defaults_to_no_discount(self) -> None:
        self.assertAlmostEqual(make_order().calculate_total(), 250)

    def test_order_total_goes_through_strategy(self) -> None:
        self.assertAlmostEqual(make_order(BulkDiscount(200, 20)).calculate_total(), 230)

    def test_set_discount_changes_strategy_on_existing_order(self) -> None:
        order = make_order(BulkDiscount(200, 20))
        order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(order.calculate_total(), 225)

    def test_two_orders_can_share_one_strategy_object(self) -> None:
        shared = PercentageDiscount(10)
        self.assertAlmostEqual(make_order(shared).calculate_total(), 225)
        self.assertAlmostEqual(make_order(shared).calculate_total(), 225)

    def test_order_contains_no_discount_type_logic(self) -> None:
        source = inspect.getsource(Order)
        self.assertNotIn("elif", source)
        self.assertNotIn("isinstance", source)


if __name__ == "__main__":
    unittest.main()
