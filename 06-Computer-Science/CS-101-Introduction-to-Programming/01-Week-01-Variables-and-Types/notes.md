# Week 01: Variables and Data Types

## 📋 Learning Objectives

By the end of this week, you will:
- Understand what variables are and how to use them
- Know the basic data types in Python (int, float, str, bool)
- Perform basic operations with different data types
- Convert between data types
- Follow Python naming conventions

---

## 1. What is a Variable?

A **variable** is a named container that stores data. Think of it like a labeled box where you can put information.

```python
# Creating a variable
message = "Hello, Python!"
age = 25
```

In this example:
- `message` is a variable that stores text
- `age` is a variable that stores a number

### Variable Assignment

```python
x = 10          # Assigns 10 to x
name = "Alice"  # Assigns "Alice" to name
```

The `=` sign is the **assignment operator**. It assigns the value on the right to the variable name on the left.

---

## 2. Python Data Types

Python has several built-in data types. Here are the most important ones for beginners:

### Integer (int)

Whole numbers, positive or negative, without decimals.

```python
age = 25
year = 2025
temperature = -5
```

### Float

Numbers with decimal points.

```python
price = 19.99
pi = 3.14159
temperature = 98.6
```

### String (str)

Text data, enclosed in quotes (single or double).

```python
name = "Alice"
greeting = 'Hello, World!'
message = "Python is awesome!"
```

#### String Quotes
```python
# Single quotes
text1 = 'Hello'

# Double quotes
text2 = "Hello"

# They're equivalent, but choose one style consistently
# Use single quotes when string contains double quotes
dialogue = 'She said "Hello"'

# Or use double quotes when string contains single quotes
contraction = "It's a beautiful day"
```

### Boolean (bool)

True or False values.

```python
is_student = True
is_raining = False
has_license = True
```

**Note**: In Python, `True` and `False` must be capitalized!

---

## 3. Checking Data Types

Use the `type()` function to check a variable's type:

```python
x = 42
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>

name = "Alice"
print(type(name))  # <class 'str'>

is_valid = True
print(type(is_valid))  # <class 'bool'>
```

See examples in: [code/data_types.py](./code/data_types.py)

---

## 4. Basic Operations

### Arithmetic Operations (Numbers)

```python
# Addition
result = 10 + 5    # 15

# Subtraction
result = 10 - 5    # 5

# Multiplication
result = 10 * 5    # 50

# Division (always returns float)
result = 10 / 5    # 2.0

# Integer Division (returns int)
result = 10 // 3   # 3

# Modulus (remainder)
result = 10 % 3    # 1

# Exponentiation
result = 2 ** 3    # 8 (2 to the power of 3)
```

### String Operations

```python
# Concatenation (combining strings)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # "John Doe"

# Repetition
laugh = "ha" * 3  # "hahaha"

# Length
name = "Alice"
length = len(name)  # 5
```

See examples in: [code/operations.py](./code/operations.py)

---

## 5. Type Conversion

Sometimes you need to convert one data type to another.

### Common Conversions

```python
# String to Integer
age_str = "25"
age_int = int(age_str)  # 25

# String to Float
price_str = "19.99"
price_float = float(price_str)  # 19.99

# Integer to String
age = 25
age_str = str(age)  # "25"

# Float to Integer (truncates decimal)
price = 19.99
price_int = int(price)  # 19 (not rounded!)
```

### Why Type Conversion Matters

```python
# This causes an error!
# age = "25"
# next_year_age = age + 1  # TypeError!

# Correct way:
age = "25"
next_year_age = int(age) + 1  # 26

# Or for output:
age = 25
message = "I am " + str(age) + " years old"
```

See examples in: [code/type_conversion.py](./code/type_conversion.py)

---

## 6. Variable Naming Rules

### Rules (must follow)

1. **Must start** with a letter or underscore
   ```python
   name = "Alice"      # ✅ Good
   _private = 42       # ✅ Good
   # 2name = "Bob"     # ❌ Error! Can't start with number
   ```

2. **Can contain** letters, numbers, and underscores
   ```python
   user_name = "alice"   # ✅ Good
   user1 = "bob"         # ✅ Good
   # user-name = "eve"   # ❌ Error! No hyphens
   ```

3. **Case sensitive**
   ```python
   name = "Alice"
   Name = "Bob"
   NAME = "Charlie"
   # These are three different variables!
   ```

4. **Cannot use** Python keywords
   ```python
   # class = "CS101"   # ❌ Error! 'class' is a keyword
   # for = 5           # ❌ Error! 'for' is a keyword
   ```

### Conventions (should follow)

1. **Use lowercase** with underscores for variables
   ```python
   user_name = "alice"     # ✅ Good (snake_case)
   # UserName = "bob"      # ⚠️  Works but not conventional
   ```

2. **Use descriptive names**
   ```python
   student_age = 20        # ✅ Clear and descriptive
   # x = 20                # ⚠️  Not clear what x represents
   ```

3. **Avoid single letters** (except for loops or math)
   ```python
   # Okay in specific contexts:
   i = 0                   # Loop counter
   x, y = 10, 20          # Coordinates
   
   # Better for general use:
   count = 0
   horizontal_position = 10
   ```

---

## 7. User Input

Get input from users with the `input()` function:

```python
# Basic input (always returns a string)
name = input("What is your name? ")
print("Hello, " + name + "!")

# Input with type conversion
age = int(input("How old are you? "))
next_year = age + 1
print("Next year you will be " + str(next_year))
```

⚠️ **Important**: `input()` always returns a **string**, even if the user types a number!

See examples in: [code/user_input.py](./code/user_input.py)

---

## 8. Comments

Comments explain code and are ignored by Python.

```python
# This is a single-line comment

age = 25  # Comments can be on the same line as code

"""
This is a multi-line comment
(actually a multi-line string, but often used as comments)
Use it for longer explanations
"""
```

### When to Use Comments

✅ **Good use of comments**:
```python
# Calculate tax (8.5% rate)
tax = price * 0.085
```

❌ **Unnecessary comments**:
```python
# Set age to 25
age = 25  # This is obvious from the code
```

---

## 9. Common Errors and Debugging

### NameError
```python
# print(age)  # NameError: name 'age' is not defined
# Fix: Define the variable first
age = 25
print(age)
```

### TypeError
```python
# age = "25"
# result = age + 5  # TypeError: can only concatenate str to str
# Fix: Convert type
age = int("25")
result = age + 5
```

### SyntaxError
```python
# message = "Hello  # SyntaxError: unterminated string
# Fix: Close the string
message = "Hello"
```

---

## 10. Practice Problems

Try these exercises (solutions in [exercises.md](./exercises.md)):

1. **Variable Creation**: Create variables for your name, age, and favorite color
2. **Calculations**: Write a program that calculates the area of a rectangle
3. **Temperature Converter**: Convert Celsius to Fahrenheit
4. **User Greeting**: Ask for user's name and age, then greet them
5. **Type Conversion**: Fix a program with type errors

---

## 📚 Additional Resources

### Official Documentation
- [Python Variables](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
- [Python Data Types](https://docs.python.org/3/library/stdtypes.html)

### Video Tutorials
- [Variables in Python - Corey Schafer](https://www.youtube.com/watch?v=ohBFZzRCr6Q)
- [Python Data Types - Programming with Mosh](https://www.youtube.com/watch?v=gCCVsvgR2KU)

### Interactive Practice
- [Python Variables - W3Schools](https://www.w3schools.com/python/python_variables.asp)
- [Python Exercises - HackerRank](https://www.hackerrank.com/domains/python)

---

## 🎯 Week Summary

This week you learned:
- ✅ How to create and use variables
- ✅ The basic data types: int, float, str, bool
- ✅ Performing operations with different types
- ✅ Converting between data types
- ✅ Naming conventions and best practices
- ✅ Getting user input

**Next Week**: Control Flow - making decisions with if statements and loops!

---

## 📝 Quick Reference

```python
# Variables
x = 10
name = "Alice"

# Data Types
age = 25                    # int
price = 19.99               # float
message = "Hello"           # str
is_valid = True             # bool

# Type Checking
type(x)                     # Returns the type

# Type Conversion
int("25")                   # String to int
float("3.14")               # String to float
str(25)                     # Int to string

# Basic Operations
10 + 5                      # Addition
10 - 5                      # Subtraction
10 * 5                      # Multiplication
10 / 5                      # Division
10 // 3                     # Integer division
10 % 3                      # Modulus
2 ** 3                      # Exponentiation

# String Operations
"Hello" + " " + "World"     # Concatenation
"ha" * 3                    # Repetition
len("Hello")                # Length

# User Input
input("Prompt: ")           # Get string input
int(input("Age: "))         # Get integer input

# Comments
# Single line comment
"""Multi-line comment"""
```

---

**Ready for next week?** → [Week 02: Control Flow](../02-Week-02-Control-Flow/)

