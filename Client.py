class Client:
    def __init__(self, client_id, name, email, address, phone_number, gender):
        self.client_id = int(client_id)
        self.name = name
        if "@" not in email:
            self.email = "tba@gmail.com"
        if "." not in email:
            self.email = "tba@gmail.com"
        if "@" and "." in email:
            self.email = email
        self.address = address
        if len(phone_number) != 10:
            self.phone_number = "0525381648"
        else:
            self.phone_number = phone_number
        if gender == "M" or gender == "F":
            self.gender = gender
        else:
            self.gender = "Other"

    def print_me(self):
        print(f"---- {self.client_id}----\n"
              f"name: {self.name}\n"
              f"email: {self.email}\n"
              f"address: {self.address}\n"
              f"phone_number: {self.phone_number}\n"
              f"gender: {self.gender}")

    def __str__(self):
        return f"{self.client_id}," \
               f" {self.name}, " \
               f"{self.email}," \
               f" {self.address}," \
               f" {self.phone_number}," \
               f" {self.gender}"

    def __repr__(self):
        return str(self)

if __name__ == "__main__":
    c = Client(1234, "Tomer", "tomer@ggg.com", "Rotschild Street", "0525381648", "5555M")
    c.print_me()
    print(c)




