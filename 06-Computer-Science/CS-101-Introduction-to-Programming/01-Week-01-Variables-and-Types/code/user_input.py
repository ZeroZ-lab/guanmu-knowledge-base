#!/usr/bin/env python3
"""
CS-101 Week 01: User Input Examples
This file demonstrates getting input from users
"""

print("=== USER INPUT EXAMPLES ===\n")

# ===== BASIC INPUT =====
print("--- Example 1: Basic String Input ---")
name = input("What is your name? ")
print(f"Hello, {name}!")
print(f"Type of name: {type(name)}")  # Always string!
print()

# ===== INPUT WITH TYPE CONVERSION =====
print("--- Example 2: Integer Input ---")
age = int(input("How old are you? "))
print(f"Next year you will be {age + 1} years old.")
print(f"Type of age: {type(age)}")
print()

print("--- Example 3: Float Input ---")
height = float(input("What is your height in meters? "))
print(f"Your height is {height}m.")
print(f"That's {height * 100}cm.")
print()

# ===== MULTIPLE INPUTS =====
print("--- Example 4: Multiple Inputs ---")
first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))

print(f"\nProfile:")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print()

# ===== PRACTICAL EXAMPLE: CALCULATOR =====
print("--- Example 5: Simple Calculator ---")
print("Let's add two numbers!")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2

print(f"{num1} + {num2} = {result}")
print()

# ===== PRACTICAL EXAMPLE: PERSONALIZED GREETING =====
print("--- Example 6: Personalized Greeting ---")
name = input("What's your name? ")
favorite_color = input("What's your favorite color? ")

print(f"\nHello, {name}!")
print(f"I love {favorite_color} too!")
print()

# ===== FORMATTED OUTPUT =====
print("--- Example 7: Formatted Report ---")
print("\n" + "=" * 40)
print("CUSTOMER INFORMATION FORM".center(40))
print("=" * 40)

customer_name = input("Name: ")
email = input("Email: ")
phone = input("Phone: ")

print("\n" + "=" * 40)
print("SUMMARY".center(40))
print("=" * 40)
print(f"Name:  {customer_name}")
print(f"Email: {email}")
print(f"Phone: {phone}")
print("=" * 40)
print()

# ===== IMPORTANT NOTES =====
print("=== IMPORTANT NOTES ===\n")
print("1. input() ALWAYS returns a string")
print("2. Convert to int or float if you need to do math")
print("3. Program waits for user to press Enter")
print("4. Use descriptive prompts to guide users")

