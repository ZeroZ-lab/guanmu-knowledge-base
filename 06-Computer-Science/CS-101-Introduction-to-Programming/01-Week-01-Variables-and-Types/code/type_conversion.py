#!/usr/bin/env python3
"""
CS-101 Week 01: Type Conversion Examples
This file demonstrates converting between different data types
"""

print("=== TYPE CONVERSION EXAMPLES ===\n")

# ===== STRING TO INTEGER =====
print("--- String to Integer ---")
age_str = "25"
print(f"Original: {age_str} (type: {type(age_str)})")

age_int = int(age_str)
print(f"Converted: {age_int} (type: {type(age_int)})")
print(f"Can now do math: {age_int} + 5 = {age_int + 5}")
print()

# ===== STRING TO FLOAT =====
print("--- String to Float ---")
price_str = "19.99"
print(f"Original: {price_str} (type: {type(price_str)})")

price_float = float(price_str)
print(f"Converted: {price_float} (type: {type(price_float)})")
print(f"Can now do math: {price_float} * 2 = {price_float * 2}")
print()

# ===== INTEGER TO STRING =====
print("--- Integer to String ---")
age = 25
print(f"Original: {age} (type: {type(age)})")

age_str = str(age)
print(f"Converted: {age_str} (type: {type(age_str)})")
print(f"Can now concatenate: 'I am ' + age_str = I am {age_str}")
print()

# ===== FLOAT TO INTEGER =====
print("--- Float to Integer ---")
price = 19.99
print(f"Original: {price} (type: {type(price)})")

price_int = int(price)
print(f"Converted: {price_int} (type: {type(price_int)})")
print("Note: Decimal is truncated, not rounded!")
print()

# ===== FLOAT TO STRING =====
print("--- Float to String ---")
pi = 3.14159
print(f"Original: {pi} (type: {type(pi)})")

pi_str = str(pi)
print(f"Converted: {pi_str} (type: {type(pi_str)})")
print()

# ===== PRACTICAL EXAMPLES =====
print("=== PRACTICAL EXAMPLES ===\n")

# Example 1: User input is always string
print("--- Example 1: Processing User Input ---")
# Simulating user input
user_input = "30"  # In real program: input("Enter your age: ")
print(f"User entered: {user_input}")

age = int(user_input)
next_year = age + 1
print(f"Next year you will be: {next_year}")
print()

# Example 2: Building a message with numbers
print("--- Example 2: Building Messages ---")
score = 95
total = 100
percentage = (score / total) * 100

message = "You scored " + str(score) + " out of " + str(total)
message += " (" + str(percentage) + "%)"
print(message)
print()

# Example 3: Mixed calculations
print("--- Example 3: Mixed Calculations ---")
item_count = "5"
item_price = "12.99"

total_cost = int(item_count) * float(item_price)
print(f"Items: {item_count}")
print(f"Price each: ${item_price}")
print(f"Total cost: ${total_cost}")
print()

# ===== COMMON ERRORS =====
print("=== COMMON ERRORS ===\n")

print("--- Error: Trying to convert non-numeric string ---")
print("int('hello') would cause: ValueError")
print()

print("--- Error: Forgetting to convert ---")
age = "25"
# This would cause TypeError: next_year = age + 1
print(f"Can't do: age('25') + 1")
print(f"Must do: int('25') + 1 = {int(age) + 1}")
print()

print("--- Error: Concatenating number with string ---")
age = 25
# This would cause TypeError: "Age: " + age
print("Can't do: 'Age: ' + 25")
print(f"Must do: 'Age: ' + str(25) = Age: {str(age)}")

