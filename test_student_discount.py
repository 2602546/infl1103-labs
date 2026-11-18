import unittest
from supplier import Supplier
from PhysicalProduct import PhysicalProduct
from order import Order
from discount_strategy import DiscountStrategy
from student_discount import StudentDiscount


class HalfPrice(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total / 2


def make_order() -> Order:
    supplier = Supplier("S001", "TechSource", "sales@techsource.com")
    product = PhysicalProduct("P001", "Lamp", 50.00, 10, supplier, 1.0)
    order = Order("O001")
    order.add_order_line(product, 5)
    return order


class TestNewStrategiesNeedNoChangeToOrder(unittest.TestCase):
    def test_student_discount_takes_five_percent_off(self) -> None:
        self.assertAlmostEqual(StudentDiscount().apply(250), 237.5)

    def test_order_accepts_student_discount(self) -> None:
        order = make_order()
        order.set_discount(StudentDiscount())
        self.assertAlmostEqual(order.calculate_total(), 237.5)

    def test_order_accepts_a_brand_new_strategy_defined_in_the_test(self) -> None:
        order = make_order()
        order.set_discount(HalfPrice())
        self.assertAlmostEqual(order.calculate_total(), 125)


if __name__ == "__main__":
    unittest.main()
