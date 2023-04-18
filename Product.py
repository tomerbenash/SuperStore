class Product:
    def __init__(self, product_id, brand, model, year, price):

        self.product_id = int(product_id)
        #self.product_type = product_type
        self.brand = brand
        self.model = model
        if len(year) != 4:
            self.year = "2010"
        else:
            self.year = year
        self.price = int(price)

    def print_me(self):
        print(f"---- {self.product_id} ----\n"
              #f"product_type: {self.product_type}\n"
              f"brand: {self.brand}\n"
              f"model: {self.model}\n"
              f"year: {self.year}\n"
              f"price: {self.price} ")

    def Is_popular(self):
        if int(self.year)>2017 and int(self.price)<3000:
            return True
        else:
            return False




    def __str__(self): # f"{self.product_type},"\
        return f"{self.product_id}," \
               f"{self.brand}," \
               f"{self.model}," \
               f"{self.year}," \
               f"{self.price}"




    def __repr__(self):
        return str(self)