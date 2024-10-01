'''
Name: Phann Boon
Date: 9/24/24
Description: More of f-strings, inputs, and numbers/ops
'''
print("My first commit!")

my_int = 5
my_float = 7.44
print(f"{my_int} {my_float}")

another_float = 8.0 # make this a float by adding .0
float_two = float(8) # make a float by casting
print(f"{another_float} {float_two}")

# get decimal from a user
radius = float(input("Enter a radius: "))
print(f"You entered a radius of {radius}")

# operations on numbers
# P E MModD AS
# modulus operator or remainder operator
print(15 % 7) # prints the remainder when 15 is divided by 7
print((2+3)*4) # 2+3 first, times 4

# exponent is not ^, it is **
print(5**4) # this is 5 to the 4th
print(5^4) # this is not

# weird stuff
print(0.3-0.2) # roundoff error - watch out for it

# rounding
# method 1, use round()
num = 3.1415
print(round(num,2))
# method 2, use f string
print(f"{num:.2f}")

# your turn to code
# Ask a user for some amount of US dollars
# Store this in a variable
# Convert that money to some currency of your choice
# Store the conversion factor in a variable
# Store the final amount in a variable
# Print is like "___ USD is the same as ___ CAD".
# Round to 2 decimal places
usd = float(input("How many USD do you want to convert to CAD? "))
usd = round(usd,2)
cad = float(usd*1.35)
cad = round(cad,2)
print(str(usd) + " USD is the same as " + str(cad) + " CAD")

# string methods
name = "lee cat"
name2 = "BOB BUILDER"
print(name.upper())
print(name.title())
print(name2.lower())