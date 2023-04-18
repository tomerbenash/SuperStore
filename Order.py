class Order:
    def __init__(self, order_id, client_id, product_id, quantity):
        self.order_id = int(order_id)
        self.client_id = int(client_id)
        self.product_id = int(product_id)
        self.quantity = int(quantity)

    def __str__(self):
        return f"{self.order_id}, " \
               f"{self.client_id}, " \
               f"{self.product_id}, " \
               f"{self.quantity} "

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    o1 = Order(199,2222222222,333,5)
    print(o1)