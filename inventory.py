from product import Product

class Inventory:
    def __init__(self) -> None:
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True

    def search_product(self, product_id: str) -> Product | None:
        for p in self.__products:
            if p.get_product_id() == product_id:
                return p
        return None

    def display_all(self):
        print("Current Inventory")
        print("------------------------------------------------")
        for p in self.__products:
            p.display_information()
        print("------------------------------------------------")

    def get_products(self):
        return self.__products