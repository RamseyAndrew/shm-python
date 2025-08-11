class Shape:
    def __init__(self, name):
        self.name = name
        
        def describe(self):
            print (f"This is a shape named {self.name}.")
            
        class Rectangle(Shape):
            def __init__(self, name, width, length):
                super().__init__("Rectangle")
                self.width = width
                self.length = length
        
        r1= Rectangle( 5, 10)
        r1.describe()
        print("name is", r1.name)
