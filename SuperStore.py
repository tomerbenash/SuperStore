import csv
from Laptop import Laptop
from Smartphone import Smartphone
from Client import Client
from Shirts import Shirts
from Order import Order
#from ShirtError import ShirtNotFoundError
#from ClientError import ClientNotFoundError

class NewSuperStore:
    def __init__(self, products, clients, shirts, orders):
        products_list = []
        clients_list = []
        orders_list = []

        with open(products) as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for row in csv_file:
                if row[1] == "laptop":
                    product_id = int(row[0])
                    brand = row[2]
                    model = row[3]
                    year = row[4]
                    price = row[5]
                    CPU = row[6]
                    hard_disk = row[7]
                    screen = row[8]

                    product = Laptop(product_id, brand, model, year, price, CPU, hard_disk, screen)
                    products_list.append(product)

                else:
                    product_id = int(row[0])
                    brand = row[2]
                    model = row[3]
                    year = row[4]
                    price = row[5]
                    cell_net = row[9]
                    num_cores = row[10]
                    cam_res = row[11]

                    product = Smartphone(product_id, brand, model, year, price, cell_net, num_cores, cam_res)
                    products_list.append(product)

        with open(clients) as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for row in csv_file:
                client_id = int(row[0])
                name = row[1]
                email = row[2]
                address = row[3]
                phone_number = row[4]
                gender = row[5]

                client = Client(client_id, name, email, address, phone_number, gender)
                clients_list.append(client)

        with open(shirts) as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for row in csv_file:
                product_id = int(row[0])
                product_name = row[1]
                price = int(row[2])
                units_in_stock = int(row[3])

                product = Shirts(product_id, '', '', '', price, product_name, units_in_stock)
                products_list.append(product)

        with open(orders) as file:
            csv_file = csv.reader(file)
            next(csv_file)
            for row in csv_file:
                order_id = int(row[0])
                client_id = int(row[1])
                product_id = int(row[2])
                quantity = int(row[3])

                order = Order(order_id, client_id, product_id, quantity)
                orders_list.append(order)

        # print(products_list)
        # print(clients_list)
        self.products = products_list
        self.clients = clients_list
        self.shirts = shirts
        self.orders = orders_list

    def print_orders(self):
        for order in self.orders:
            print(order)

    def get_orders(self):
        orders_list = []
        for order in self.orders:
            orders_list.append(order)
            return orders_list

    def get_all_shirts(self):
        shirts_list = []
        for product in self.products:
            if type(product) is Shirts:
                shirts_list.append(product)
        return shirts_list

    def print_products(self):
        for item in self.products:
            print(item)

    def get_product(self, product_id):
        for item in self.products:
            if product_id == item.product_id:
                return item

    def remove_product(self, product_id):
        for item in self.products:
            if product_id == item.product_id:
                print(f"item with id {product_id} removed successfully")
                self.products.remove(item)
                return True
        print(f"product with id {product_id} doesn't exists, can't delete")
        return False

    def get_all_by_brand(self, brand):
        brand_list = []
        for item in self.products:
            if brand == item.brand:
                brand_list.append(item)
        print(f"{brand}'s list:")
        return brand_list

    def get_all_by_price_under(self, price):
        all_by_price_under = []
        for item in self.products:
            if int(price) > int(item.price):
                all_by_price_under.append(item)
        print(f"Products under {price} are")
        return all_by_price_under

    def get_most_expensive_product(self, price):
        for item in self.products:
            if int(price) < int(item.price):
                price = item.price
        for item in self.products:
            if price == item.price:
                print(f"The most expensive product costs {price}")
                return item

    def print_clients(self):
        for client in self.clients:
            print(client)

    def get_all_clients(self):
        clients_list = []
        for client in self.clients:
            clients_list.append(client)
        return clients_list

    def get_client(self, client_id):
        for client in self.clients:
            if client_id == client.client_id:
                return client.client_id, client.name, client.address, client.email, client.phone_number, client.gender

    def get_full_client(self, client_id):
        for client in self.clients:
            if client_id == client.client_id:
                return client

    def add_client(self, new_client):
        for client in self.clients:
            if new_client.client_id == client.client_id:
                print(f"client with id {new_client.client_id} already exists, can't add")
                return False
        self.clients.append(new_client)
        print(f"Client with id {new_client.client_id} added successfully")
        return True

    def remove_client(self, client_id):
        for client in self.clients:
            if client_id == client.client_id:
                print(f"Client with id {client_id} removed successfully")
                self.clients.remove(client)
                return True
        print(f"Client with id {client_id} doesn't exists, can't delete")
        return False

    def get_all_phones(self):
        phones_list = []
        for product in self.products:
            if type(product) is Smartphone:
                phones_list.append(product)
        # return f"The smartphones list:\n" \
        #        f"{phones_list}"

        # phones_list_str = '\n'.join(map(str, phones_list))
        # return phones_list_str

        return phones_list

    def get_all_laptops(self):
        laptops_list = []
        for product in self.products:
            if type(product) is Laptop:
                laptops_list.append(product)
        # return f"The laptops list:\n" \
        #        f"{laptops_list}"

        # laptops_list_str = '\n'.join(map(str, laptops_list))
        # return laptops_list_str
        return laptops_list


    def phone_average_price(self):
        price_counter = 0
        smartphone_counter = 0
        for product in self.products:
            if type(product) is Smartphone:
                price_counter += int(product.price)
                smartphone_counter += 1
        return f"The average phone price is: {price_counter / smartphone_counter}"

    def get_max_screen(self):
        screen_size = 0
        for product in self.products:
            if type(product) is Laptop:
                if screen_size < int(product.screen):
                    screen_size = int(product.screen)
        return f"The biggest laptop screen is: {screen_size}"

    def get_common_cam(self):
        from collections import Counter
        common_list = []
        for product in self.products:
            if type(product) is Smartphone:
                common_list.append(product.cam_res)
        counter = Counter(common_list)
        return f"The most common cam resolution is: {counter.most_common(1)[0][0]}"

    def list_popular(self):
        popular_list = []
        for product in self.products:
            if product.Is_popular():
                popular_list.append(product)
        return f"This is the popular list:\n" \
               f"{popular_list}"

    # def add_product_new(self, new_product):
    #     for product in self.products:
    #         if new_product.product_id == product.product_id:
    #             print(f"product with id {new_product.product_id} already exists, can't add")
    #             return False
    #     self.products.append(other)
    #     print(f"product with id {new_product.product_id} added successfully")
    #     return True

    def __iadd__(self, other):
        for product in self.products:
            if other.product_id == product.product_id:
                print(f"product with id {other.product_id} already exists, can't add")
                return self
        self.products.append(other)
        print(f"product with id {other.product_id} added successfully")
        return self

    def get_shirt(self, product_id):
        for product in self.products:
            if type(product) is Shirts:
                if product_id == product.product_id:
                    return product

    def get_max_order_id(self):
        order_id_list = []
        for order in self.orders:
            order_id_list.append(order.order_id)
        return max(order_id_list)

    # def get_all_shirts(self):
    #     for product in self.products:
    #         if type(product) is Shirts:
    #             print(product)

    def add_order(self, client_id, product_id, amount):

        try:
            client = self.get_full_client(client_id)
            if not client:
                raise ClientNotFoundError()

            product = self.get_product(product_id)
            if not product:
                raise ShirtNotFoundError()
            if type(product) is Laptop or type(product) is Smartphone:
                if amount > 1:
                    raise ValueError("Order too big, not enough in stock")
            if type(product) is Shirts:
                if amount > product.units_in_stock:
                    raise ValueError("Order too big, not enough in stockzzzzz")


            order_id = self.get_max_order_id() + 1
            new_order = Order(order_id, client_id, product_id, amount)
            self.orders.append(new_order)
            print("Order confirmed")


        except Exception as e:
            print(e)

newsuper = NewSuperStore('products_supply.csv', 'clients.csv', 'shirts.csv', 'orders.csv')



#print(newsuper.get_all_shirts())