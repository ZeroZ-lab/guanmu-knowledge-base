#!/usr/bin/env python3
"""
CS-101 Week 01: Operations Examples
This file demonstrates basic operations with different data types
"""

# ===== ARITHMETIC OPERATIONS =====
print("=== ARITHMETIC OPERATIONS ===")

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Integer Division: {a} // {b} = {a // b}")
print(f"Modulus (Remainder): {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")
print()

# ===== ORDER OF OPERATIONS =====
print("=== ORDER OF OPERATIONS (PEMDAS) ===")
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}  # Multiplication first")

result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}  # Parentheses first")

result3 = 10 + 5 * 2 - 3 / 3
print(f"10 + 5 * 2 - 3 / 3 = {result3}")
print()

# ===== STRING OPERATIONS =====
print("=== STRING OPERATIONS ===")

# Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"First: {first_name}")
print(f"Last: {last_name}")
print(f"Full: {full_name}")
print()

# Repetition
laugh = "ha" * 3
border = "-" * 20
print(f"Laugh: {laugh}")
print(border)
print()

# Length
name = "Alice"
name_length = len(name)
print(f"Name: {name}")
print(f"Length: {name_length}")
print()

# ===== COMBINING DIFFERENT OPERATIONS =====
print("=== PRACTICAL EXAMPLES ===")

# Calculate area of a rectangle
length = 5
width = 3
area = length * width
print(f"Rectangle: {length} x {width}")
print(f"Area: {area}")
print()

# Format a price tag
item = "Coffee"
price = 4.50
quantity = 2
total = price * quantity
message = item + ": $" + str(price) + " x " + str(quantity) + " = $" + str(total)
print(message)
print()

# Build a simple report
print("=" * 30)
print("SALES REPORT".center(30))
print("=" * 30)
print(f"Item: {item}")
print(f"Price: ${price}")
print(f"Quantity: {quantity}")
print(f"Total: ${total}")
print("=" * 30)

