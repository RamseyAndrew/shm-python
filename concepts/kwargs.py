
## *kwargs -> Key word arguments
## Dictionary{key:value}

# 3 min :try mixing up
def greet(name,nationality):
    print("Name is",name)
    print("From ",nationality)

## Kwargs solve the mixup
greet("John","India")

greet(nationality="Babylon",name="Samson")