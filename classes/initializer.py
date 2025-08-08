class Human:
    def __init__(self, gender, age, name):
        print("Hello, I am a human!")
        print("Gender:", gender)
        print("Age:", age)
        print("Name:", name)

def another_one():
    print("I am another human!")

# Create a Human instance
adam = Human(name="Adam", age=24, gender="Male")

# Call the function
another_one()
