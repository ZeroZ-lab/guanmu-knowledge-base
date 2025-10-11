#!/usr/bin/env python3
"""
CS-101 Week 01: Data Types Examples
This file demonstrates different data types in Python
"""

# ===== INTEGER (int) =====
print("=== INTEGER EXAMPLES ===")
age = 25
year = 2025
negative_num = -42

print(f"age: {age}, type: {type(age)}")
print(f"year: {year}, type: {type(year)}")
print(f"negative_num: {negative_num}, type: {type(negative_num)}")
print()

# ===== FLOAT =====
print("=== FLOAT EXAMPLES ===")
price = 19.99
pi = 3.14159
temperature = -5.5

print(f"price: {price}, type: {type(price)}")
print(f"pi: {pi}, type: {type(pi)}")
print(f"temperature: {temperature}, type: {type(temperature)}")
print()

# ===== STRING (str) =====
print("=== STRING EXAMPLES ===")
name = "Alice"
greeting = 'Hello, World!'
message = "Python is awesome!"

print(f"name: {name}, type: {type(name)}")
print(f"greeting: {greeting}, type: {type(greeting)}")
print(f"message: {message}, type: {type(message)}")
print()

# String with quotes inside
dialogue = 'She said "Hello"'
contraction = "It's a beautiful day"
print(f"dialogue: {dialogue}")
print(f"contraction: {contraction}")
print()

# ===== BOOLEAN (bool) =====
print("=== BOOLEAN EXAMPLES ===")
is_student = True
is_raining = False
has_license = True

print(f"is_student: {is_student}, type: {type(is_student)}")
print(f"is_raining: {is_raining}, type: {type(is_raining)}")
print(f"has_license: {has_license}, type: {type(has_license)}")
print()

# ===== CHECKING TYPES =====
print("=== TYPE CHECKING ===")
x = 42
print(f"The type of {x} is: {type(x)}")

y = 3.14
print(f"The type of {y} is: {type(y)}")

name = "Alice"
print(f"The type of '{name}' is: {type(name)}")

flag = True
print(f"The type of {flag} is: {type(flag)}")

