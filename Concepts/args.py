
# your function only takes 3 parameters
# your function 4 or 5 or 6
#Args -> arguments
#def stuff(name,age,gender,is_married):


def  greet(*args):
    for value in args:
        print("Name is",value)
        
greet("John","Samuel","Mandy")