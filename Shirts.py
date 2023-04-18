from Product import Product

class Shirts(Product):
    def __init__(self, product_id, brand, model, year, price, product_name, units_in_stock):
        super().__init__(product_id, brand, model, year, price,)
        self.brand = "SuperStore"
        self.model = ""
        self.year = 2023
        self.product_name = product_name
        self.units_in_stock = int(units_in_stock)

    def __str__(self):
        #parent_str = super().__str__()
        return f"{self.product_id}," \
               f"{self.product_name}," \
               f"{self.price}," \
               f"{self.units_in_stock}"

    def __repr__(self):
        return str(self)



if __name__ == "__main__":
    s1 = Shirts(203, "d", "d", "2", 1009,"Romero", 20)

    print(s1)

    print(s1)

