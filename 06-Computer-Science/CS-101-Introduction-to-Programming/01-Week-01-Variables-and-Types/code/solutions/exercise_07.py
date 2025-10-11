#!/usr/bin/env python3
"""
Exercise 7: Temperature Converter
Convert Celsius to Fahrenheit and Kelvin
"""

# Get temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = (celsius * 9/5) + 32

# Convert to Kelvin (bonus)
kelvin = celsius + 273.15

# Print results
print(f"{celsius}°C is equal to {fahrenheit}°F")
print(f"{celsius}°C is equal to {kelvin}K")

