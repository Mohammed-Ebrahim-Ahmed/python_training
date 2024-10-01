x = 2

class JustNotCoolError(Exception):
    pass
try:
    raise JustNotCoolError("This just isn't cool, man.")
    # raise Exception("I'm a custom execption!")
    #print(x/0)
    # if not type(x) is str:
    #     raise TypeError()
except NameError:
    print("Name Error means someting is probably undefined.")
except ZeroDivisionError:
    print("Please do not divide by zero")
except Exception as error:
    print(error)
else:
    print("No error!")
finally:
    print("I'm going to print with or without error.")