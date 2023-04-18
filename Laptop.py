
from Product import Product
class Laptop(Product):
    def __init__(self, product_id, brand, model, year, price, CPU, hard_disk, screen):
        super().__init__(product_id, brand, model, year, price,)
        self.CPU = CPU
        self.hard_disk = int(hard_disk)
        self.screen = int(screen)

    def print_me(self):
        super().print_me()
        print(f"CPU: {self.CPU}\n"
              f"hard_disk: {self.hard_disk}\n"
              f"screen: {self.screen}")

    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str}," \
                f"{self.CPU}," \
                f"{self.hard_disk}," \
                f"{self.screen}"

    def __repr__(self):
        return str(self)



if __name__ == "__main__":
    l1 = Laptop('25969234','Apple','MacBook 1','202','83','Intel Core i7','24','2000')
    l1.print_me()
    print("")

    print(l1)
    print("")

    print(l1.Is_popular())