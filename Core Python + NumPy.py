
# Python Basics + NumPy (Cleaned & Complete)


# 1. Hello World & Version
print("Hello World")
import sys
print(sys.version)

# 2. Variables & Naming Rules
num = 5
square = num * num
print(square)          # 25

# Valid names
abc = "hello"
_abc = "hello"
print(abc)

# Invalid: 1abc = "hello"  → SyntaxError

# 3. Data Types
x = 2
print(x, type(x))          # int

y = 2.5
print(y, type(y))          # float

x = "amrit"
print(x, type(x))          # str

x = 2 + 3j
print(x, type(x))          # complex

x = (1, 2, 3)
print(x, type(x))          # tuple

x = [10, 20, 30]
print(x, type(x))          # list

x = {10, 20, 30}
print(x, type(x))          # set

x = {'a': 20, 'b': 30}
print(x, type(x))          # dict

# 4. Operators
a, b = 5, 3
print(a + b)   # 8
print(a - b)   # 2
print(a * b)   # 15
print(a / b)   # 1.666...
print(19 % 3)  # 1
print(5 ** 3)  # 125

# 5. Built-in Functions
x, y = 10, 5
print(eval('x + y * 2'))   # 20
print(abs(-10))            # 10
print(sum([1, 2, 3, 4, 5]))# 15
print(pow(285.12, 3))

# Input (always returns str)
age = input("Please enter your age: ")
print(age, type(age))

# Type conversion
age_int = int(input("Please enter your age: "))
print(age_int, type(age_int))

price = float(input("Please enter price: "))
print(price, type(price))

print(len("Hello im a   student"))  # 20

# 6. Control Flow
age = 18
if age >= 18:
    print("You are an adult.")

i = 20
if i > 10:
    print("10 is less than 20")
print("I am outside the block")

i = 5
if i > 10:
    print("i is greater than 10")
else:
    print("i is 10 or less")

score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

# 7. Loops
for i in range(3):
    print("Loop number:", i)

countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")

for i in range(1, 6):
    print(f"Line number {i}")

# Break
for i in range(10):
    if i == 5:
        break
    print(i)          # prints 0-4

# Continue
for i in range(10):
    if i == 5:
        continue
    print(i)          # skips 5
print("Hello")

# 8. Functions
def greet():
    print("Hello Nepal")
greet()

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("dog", "Buddy")
describe_pet(pet_name="Buddy", animal_type="dog")  # keyword args

# Quick demo (no input needed)
for i in range(3):
    name = f"User {i+1}"
    n = 100 + (i * 50)
    bill = n * 5
    print(f"Hi {name}, you need to pay Rs. {bill}")

# 9. Strings
single = 'Hello'
double = "World"
multiline = """This is a
multi-line string."""

text = "Python"
print(text[0:4])   # Pyth
print(text[:3])    # Pyt
print(text[2:])    # thon

message = "Welcome to Python programming!"
if "Python" in message:
    print("Found it!")
if "Java" not in message:
    print("Java is not in the text.")

print("Python 3.x".upper())
print("PLEASE STOP SHOUTING!".lower())
print("Hello world".replace('H', '3'))
print("Hello" + "world")

# 10. Lists, Tuples, Dicts, Sets
fruits = ["apple", "banana", "cherry"]
mixed = [42, "hello", True, 3.14]
print(fruits[0], fruits[2])

c = [10, 20, 30, 40, 50, 60]
print(c[2:5])               # [30, 40, 50]

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

user_profile = ("Alice", 28, "programmer")
name, age, profession = user_profile
print(name, age, profession)

car = {"brand": "Toyota", "year": 2020}
car["year"] = 2024
car["color"] = "red"
print(car)

user = dict(name="Alice", age=25, country="Nepal")
print(user)

my_set = {1, 2, 3, 3, 2}
print(my_set)               # {1, 2, 3}
unique = set([1, 2, 2, 3, 4, 4, 4, 5])
print(unique)

# 11. NumPy
import numpy as np

vector = np.array([1, 2, 3, 4])
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)         # (2, 3)

a = [1, 2, 3, 4]
b = np.array([1, 2, 3, 4])
print(a)
print(b)

print(np.zeros(3))
print(np.ones(4))
print(np.arange(0, 10))

arr = np.array([[1, 2, 3], [3, 4, 5]])
print(arr)

array_5d = np.arange(1, 33).reshape(2, 2, 2, 2, 2)
print(array_5d)