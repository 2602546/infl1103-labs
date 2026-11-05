class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
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