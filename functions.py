def hello_world():
    print("Hello world")
    
hello_world()

def sum(num1=0, num2=0):
    if (not isinstance(num1, int) or not isinstance(num2, int)):
        return 0
    return num1+num2

total = sum(7,3)
print(total)
    

def multiple_items(*args):
    print(args)
    print(type(args))
    
    
multiple_items("Dave", "John", "Sara")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
mult_named_items(first= "Dave", last = "Grey")
