# Ecomerce

class User():
    
    def __init__(self, name, email, phone, password, user, discount=0):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        self.discount = discount
        self.user = user
        self.is_locked = False

    def say_my_name(self):
        print(f"My name is {self.name}")

    def print_details(self):
        print("------------------")
        print("user", self.user)
        print("Name", self.name)
        print("Email", self.email)
        print("Phone", self.phone)
        print("Password", self.password)
        print("Discount", self.discount)
        print("------------------")

    def login(self):
        if self.is_locked:
            print("Account is locked. Please contact support.")
            return
        
        for i in range(1, 3):
            password = input(f"Enter your password: Attempt {i} ")
            if self.password == password:
                print("Login successful")
                return 
        self.is_locked = True
        print("Login failed. Account is locked.")

class Employee(User):
    def __init__(self, name, email, phone, password, salary):
        super().__init__(name, email, phone, password, user="Employee")
        self.salary = salary

class Customer(User):
    def __init__(self, name, email, phone, password):
        super().__init__(name, email, phone, password, user="Customer")