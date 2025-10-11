# Week 01: Exercises

## 📝 Practice Problems

Complete these exercises to reinforce your understanding of variables and data types.

---

## Exercise 1: Variable Creation ⭐

**Goal**: Practice creating different types of variables.

**Instructions**:
1. Create a variable called `name` and assign your name to it (as a string)
2. Create a variable called `age` and assign your age to it (as an integer)
3. Create a variable called `height` and assign your height in meters (as a float)
4. Create a variable called `is_student` and assign True or False
5. Print all four variables

**Example Output**:
```
Alice
25
1.65
True
```

**Solution**: See [code/solutions/exercise_01.py](./code/solutions/exercise_01.py)

---

## Exercise 2: Simple Calculator ⭐

**Goal**: Practice arithmetic operations.

**Instructions**:
Create a program that:
1. Defines two numbers: `a = 15` and `b = 4`
2. Calculates and prints:
   - Sum (a + b)
   - Difference (a - b)
   - Product (a * b)
   - Division (a / b)
   - Integer division (a // b)
   - Remainder (a % b)
   - Power (a ** b)

**Example Output**:
```
Sum: 19
Difference: 11
Product: 60
Division: 3.75
Integer Division: 3
Remainder: 3
Power: 50625
```

**Solution**: See [code/solutions/exercise_02.py](./code/solutions/exercise_02.py)

---

## Exercise 3: String Manipulation ⭐

**Goal**: Practice working with strings.

**Instructions**:
1. Create a variable `first_name` with your first name
2. Create a variable `last_name` with your last name
3. Create a variable `full_name` by combining first and last name with a space
4. Print the full name
5. Print the length of the full name
6. Create a variable `greeting` that says "Hello, [full_name]!"
7. Print the greeting

**Example Output**:
```
Alice Johnson
13
Hello, Alice Johnson!
```

**Solution**: See [code/solutions/exercise_03.py](./code/solutions/exercise_03.py)

---

## Exercise 4: Type Conversion ⭐⭐

**Goal**: Practice converting between data types.

**Instructions**:
1. Start with `age_str = "25"`
2. Convert it to an integer and add 5, store in `future_age`
3. Convert `future_age` back to a string and concatenate with " years old"
4. Print the result

Then:
5. Start with `price = 19.99`
6. Convert it to an integer (it will truncate the decimal)
7. Print both the original and converted values

**Example Output**:
```
30 years old
Original price: 19.99
Converted price: 19
```

**Solution**: See [code/solutions/exercise_04.py](./code/solutions/exercise_04.py)

---

## Exercise 5: User Input ⭐⭐

**Goal**: Get input from the user and use it.

**Instructions**:
Create a program that:
1. Asks the user for their name
2. Asks the user for their age (convert to integer)
3. Calculates how old they will be in 5 years
4. Prints a message like: "Hello [name]! In 5 years, you will be [age] years old."

**Example Interaction**:
```
What is your name? Alice
How old are you? 25
Hello Alice! In 5 years, you will be 30 years old.
```

**Solution**: See [code/solutions/exercise_05.py](./code/solutions/exercise_05.py)

---

## Exercise 6: Rectangle Calculator ⭐⭐

**Goal**: Combine multiple concepts.

**Instructions**:
Create a program that:
1. Asks the user for the length of a rectangle (as a float)
2. Asks the user for the width of a rectangle (as a float)
3. Calculates the area (length × width)
4. Calculates the perimeter (2 × (length + width))
5. Prints both results with appropriate labels

**Example Interaction**:
```
Enter the length: 5.5
Enter the width: 3.2
Area: 17.6
Perimeter: 17.4
```

**Solution**: See [code/solutions/exercise_06.py](./code/solutions/exercise_06.py)

---

## Exercise 7: Temperature Converter ⭐⭐

**Goal**: Build a practical conversion tool.

**Instructions**:
Create a program that:
1. Asks the user for a temperature in Celsius
2. Converts it to Fahrenheit using the formula: F = (C × 9/5) + 32
3. Prints the result

**Example Interaction**:
```
Enter temperature in Celsius: 25
25.0°C is equal to 77.0°F
```

**Bonus**: Also convert to Kelvin (K = C + 273.15)

**Solution**: See [code/solutions/exercise_07.py](./code/solutions/exercise_07.py)

---

## Exercise 8: Debug the Code ⭐⭐⭐

**Goal**: Practice identifying and fixing errors.

**Instructions**:
The following code has several errors. Find and fix them:

```python
# This code has multiple errors!
name = Alice
age = "25"
print("Name: " + name)
print("Age: " + age)
print("Next year: " + age + 1)
```

**Expected Output**:
```
Name: Alice
Age: 25
Next year: 26
```

**Hints**:
- Check string quotes
- Check data types for mathematical operations
- Think about type conversion

**Solution**: See [code/solutions/exercise_08.py](./code/solutions/exercise_08.py)

---

## Exercise 9: Swap Variables ⭐⭐⭐

**Goal**: Learn a useful programming technique.

**Instructions**:
Given two variables:
```python
a = 10
b = 20
```

Swap their values so that `a` becomes 20 and `b` becomes 10.
Print both variables before and after swapping.

**Hints**:
- You might need a temporary variable
- Or research Python's special way to swap variables in one line!

**Example Output**:
```
Before swap: a = 10, b = 20
After swap: a = 20, b = 10
```

**Solution**: See [code/solutions/exercise_09.py](./code/solutions/exercise_09.py)

---

## Exercise 10: Personal Info Card ⭐⭐⭐

**Goal**: Combine all concepts into a small project.

**Instructions**:
Create a program that:
1. Asks for the user's first name
2. Asks for the user's last name
3. Asks for the user's age
4. Asks for the user's favorite color
5. Creates a nicely formatted "info card" that displays all this information

**Example Interaction**:
```
First name: Alice
Last name: Johnson
Age: 25
Favorite color: Blue

=============================
       PERSONAL INFO
=============================
Name: Alice Johnson
Age: 25 years old
Favorite Color: Blue
=============================
```

**Bonus Challenges**:
- Make the card even nicer with ASCII art
- Add more information (city, hobby, etc.)
- Calculate birth year from age

**Solution**: See [code/solutions/exercise_10.py](./code/solutions/exercise_10.py)

---

## 🏆 Challenge Problems

### Challenge 1: Circle Calculator ⭐⭐⭐

Calculate the area and circumference of a circle given the radius.
- Area = π × r²
- Circumference = 2 × π × r
- Use 3.14159 for π

### Challenge 2: Time Converter ⭐⭐⭐

Convert a number of seconds to hours, minutes, and seconds.
Example: 3665 seconds = 1 hour, 1 minute, 5 seconds

Hint: Use integer division (//) and modulus (%)

### Challenge 3: Cost Calculator ⭐⭐⭐⭐

Ask for:
- Item price
- Quantity
- Tax rate (as a percentage)

Calculate and display:
- Subtotal
- Tax amount
- Total

---

## 💡 Tips for Success

1. **Don't just read** - type out every example
2. **Experiment** - try changing values and see what happens
3. **Use print()** liberally to see what's happening
4. **Read error messages** - they tell you what's wrong
5. **Compare your solution** with the provided ones after attempting

---

## ✅ Self-Check

Before moving to Week 02, make sure you can:

- [ ] Create variables of different types
- [ ] Use all basic arithmetic operators
- [ ] Concatenate strings
- [ ] Convert between int, float, and str
- [ ] Use the `input()` function
- [ ] Write comments
- [ ] Understand and fix common errors

---

## 📚 Additional Practice

Want more practice? Try these platforms:

- [HackerRank - Python Basics](https://www.hackerrank.com/domains/python)
- [Codewars - Python](https://www.codewars.com/)
- [Exercism - Python Track](https://exercism.org/tracks/python)

---

**Completed the exercises?** Check your solutions against [code/solutions/](./code/solutions/)

**Ready for more?** → [Week 02: Control Flow](../02-Week-02-Control-Flow/)

