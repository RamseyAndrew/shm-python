


# Ecomerce

class User():
    def __init__(self, name, email, phone, password, discount=0, type="user"):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password
        
        self.discount = discount

       

        def say_my_name(self):
            print(f"My name is {self.name}")

        def print_details(self):
            print("user",self.user)
            print("Name",self.name)
            print("Email",self.email)
            print("Phone",self.phone)
            print("Password",self.password)
            print("Discount",self.discount)

        def login(self):
            for i in range(0,3):
                password=input(f"Enter your password:")
                if self.password==password:
                    print("Login successful")
                    return 
                self.is_locked=True
            print("Login failed. Account is locked.")

            
    
    class Employee(User):
        def __init__(self, name, email, phone, password, salary):
            super().__init__(name, email, phone, password)
            self.salary=salary


    class Customer(User):
        def __init__(self, name, email, phone, password):
            super().__init__(name, email, phone, password)