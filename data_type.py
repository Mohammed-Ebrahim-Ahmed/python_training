import math 

# String data type

# literal assignment


first = "Dave"
last = "Gray"

# print(type(first))
# print(type(first) is str)
# print(isinstance(first, str))


# constructor function

# pizza = str("Pepperoni")

# print(type(pizza))
# print(type(pizza) is str)
# print(isinstance(pizza, str))

# Concatenatin

fullname = first + " " + last
fullname += "!"
print(fullname)

decade = str(123)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + "s."
print(statement)

multiline = """Hey, how are you?

I was jsut checking in?

                        All good?"""

print(multiline)


sentence = "I'm back at work!\tHey\n\n Where i's this at \\located?"

print(sentence)

# String methods

print(first)
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)


print(len(multiline))

multiline += "                                   "
multiline = "                " + multiline

# multiline += "kk"

# multiline ="kk" + multiline
print(len(multiline))


print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

string = multiline.strip()
# string = multiline+"kk"
print(string)

print("")

# Build a menu

title = "menu".upper()
print(title.center(20, "="))

print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Chessecake".ljust(16, ".") + "$3".rjust(4))

# string index value
print(first[0])
print(first[-1])
print(first[1:-1])
print(first[1:])


# Some methodes return boolean data

print(first.startswith("D"))
print(first.endswith("z"))

# Boolen data type
myvalue = True
x = bool(False)
o = type(x)

print(isinstance(x, bool))


# integer

price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price, int))

# float

gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex type

comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)


# Built-in function for number

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))


# math module
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# cast string to number

zip = "1001"
zip_value = int(zip)
print(type(zip_value))

# error

# print(int("new york"))

