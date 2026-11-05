from product import Product

class SubscriptionProduct(Product):
    def __init__(self, product_id, name, price, stock, duration_months):
        super().__init__(product_id, name, price, stock)
        self.__duration_months = duration_months
 
    def get_duration_months(self):
        return self.__duration_months
 
    def display_information(self):
        super().display_information()
        print("    Type: Subscription | Duration: %d months" % self.__duration_months)