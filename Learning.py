# Variables
Watch_price = 500

Customer_Name = "prasanth"

Watch1_Price = "$200.50"
Watch2_price = 500
Watch1_Color = "White Watch"
Watch2_Color = "Black Watch"
print(Customer_Name)
print(Watch1_Color, Watch1_Price)

Laptop_Name = "Lenovo"
Laptop_color, Laptop_price = "Navy Blue", "$200.00"
print(Laptop_Name)
print(Laptop_color, Laptop_price)

# Strings

Demon = "         Demon fight with god"

print(Demon.strip())

print(Demon[20:29])
print(len(Demon))
print(Demon.strip().upper())
print(Demon.lower().strip())
print(Demon.strip().removesuffix("d"))
print(Demon.replace("god", "king"))
print(Demon in "fire")

# Operators
# Arithmetic
# Assignment - =
# comparison - > < >= <= ===
# Logical - and or not
# Identity - Is Is not
# Membership - In not In
# byt wise - & | ^ ~ >> <<


number1 = 10
number2 = number1 + 10
number1 += 34
print(number1 + number2)

# Castings

a = 10
b = 23.8
print(a + b)

a1 = float(10)
b1 = int(12.66)
c1 = str('value')
print(a1, b1, len(c1))

# List
# we can separate add or remove in the list using []

fruits = ["apple", "orange", "cherry"]
print(fruits)
print(fruits[2])
fruits[2] = "banana"
print(fruits)

number = [65, 89, 0, 11, 55]
number.sort(reverse=True)
print(number)

# If statement

age = 19
if age > 18:
    print("Please Enter the game")
elif age == 18:
    print("You are eligible to buy the game")
else:
    print("you are denied")

# Or

a, b = 17, 18
if a == 18 or b == 19:
    print("correct")
else:
    print("Incorrect")

# And

a, b = 17, 18
if a == 17 and b == 18:
    print("correct")
else:
    print("Incorrect")

# Nesting of If

age1 = 18
if age1 == 18:
    print("Hi Rajesh")
    if age1 == 18:
        print("Welcome!, Please you can vote now")
    else:
        print("your name is not register in the voter ID")


# Functions

def addition(c, d):
    print(c + d)
addition(10, 30)
addition(200, 50)

def hi(Name):
    print("Hi," + Name)


hi("prasanth")

# Loops

name = "karthick"
for letters in name:
    print(letters)

for i in 'Hello, karthick':
    if i == ',':
        print(", is present")
for
