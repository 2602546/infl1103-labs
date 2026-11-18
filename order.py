from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount


class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def get_order_id(self) -> str:
        return self.__order_id

    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        for line in self.__order_lines:
            if line.get_product().get_product_id() == product_id:
                self.__order_lines.remove(line)
                return True
        return False

    def calculate_subtotal(self) -> float:
        total = 0.0
        for line in self.__order_lines:
            total += line.calculate_subtotal()
        return total

    def calculate_total(self) -> float:
        return self.__discount.apply(self.calculate_subtotal())

    def display_order(self) -> None:
        print("Order:", self.__order_id)
        print("------------------------------------------------")
        for line in self.__order_lines:
            line.display_information()
        print("Subtotal: $%.2f" % self.calculate_subtotal())
        print("Total after discount: $%.2f" % self.calculate_total())
        print("------------------------------------------------")
