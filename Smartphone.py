from Product import Product

class Smartphone(Product):
    def __init__(self, product_id, brand, model, year, price, cell_net, num_cores, cam_res):
        super().__init__(product_id, brand, model, year, price,)
        self.cell_net = cell_net
        self.num_cores = int(num_cores)
        self.cam_res = int(cam_res)

    def print_me(self):
        super().print_me()
        print(f"cell_net: {self.cell_net}\n"
              f"num_cores: {self.num_cores}\n"
              f"cam_res: {self.cam_res}")

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}," \
                f"{self.cell_net}," \
                f"{self.num_cores}," \
                f"{self.cam_res}"

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    s1 = Smartphone('61410094','Google','Pixel 2','2017','3606','3G','8','128')
    s1.print_me()
    print("")
    print(s1)