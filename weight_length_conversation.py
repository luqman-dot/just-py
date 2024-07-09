import sys
import math

# Function to delete the last line in the STDOUT
def delete_last_lines(n=1):
    for _ in range(n):
        sys.stdout.write('\x1b[1A')  # Cursor up one line
        sys.stdout.write('\x1b[2K')  # Delete last line

# Function to round up a number to a specific number of decimal places
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

# Conversion constants
conversion_factors = {
    "pound": {
        "ounce": 16,
        "gram": 453.592,
        "milligram": 453592,
        "kilogram": 0.453592,
    },
    "ounce": {
        "pound": 0.0625,
        "kilogram": 0.0283495,
        "milligram": 28349.5,
        "gram": 28.3495,
    },
    "gram": {
        "pound": 0.00220462,
        "kilogram": 0.001,
        "milligram": 1000,
        "ounce": 0.035274,
    },
    "kilogram": {
        "pound": 2.20462,
        "ounce": 35.274,
        "milligram": 1000000,
        "gram": 1000,
    },
    "milligram": {
        "pound": 2.20462e-6,
        "ounce": 3.5274e-5,
        "kilogram": 1e-6,
        "gram": 0.001,
    },
    "yard": {
        "inch": 36,
        "foot": 3,
        "meter": 0.9144,
        "centimeter": 91.44,
        "kilometer": 0.0009144,
        "mile": 0.000568182,
    },
    "inch": {
        "yard": 0.0277778,
        "foot": 0.0833333,
        "meter": 0.0254,
        "centimeter": 2.54,
        "kilometer": 2.54e-5,
        "mile": 1.57828e-5,
    },
    "foot": {
        "yard": 0.333333,
        "inch": 12,
        "meter": 0.3048,
        "centimeter": 30.48,
        "kilometer": 0.0003048,
        "mile": 0.000189394,
    },
    "meter": {
        "yard": 1.09361,
        "foot": 3.28084,
        "inch": 39.3701,
        "centimeter": 100,
        "kilometer": 0.001,
        "mile": 0.000621371,
    },
    "centimeter": {
        "yard": 0.0109361,
        "foot": 0.0328084,
        "inch": 0.393701,
        "meter": 0.01,
        "kilometer": 1e-5,
        "mile": 6.21371e-6,
    },
    "kilometer": {
        "yard": 1093.61,
        "foot": 3280.84,
        "inch": 39370.1,
        "meter": 1000,
        "centimeter": 100000,
        "mile": 0.621371,
    },
    "mile": {
        "yard": 1760,
        "foot": 5280,
        "inch": 63360,
        "meter": 1609.34,
        "centimeter": 160934,
        "kilometer": 1.60934,
    }
}

# Function to print the available options
def print_options():
    print("Length Options:")
    print("Yard, Foot, Inch, Meter, Centimeter, Kilometer, Mile")
    print()
    print("Weight Options:")
    print("Pound, Gram, Milligram, Ounce, Kilogram")
    print()

print_options()

# Get user input for conversion type
conversion_type = input("Would you like to convert weight or length?: ").strip().lower()

# Get user input for units and measure
unit_from = input("What is your first unit?: ").strip().lower()
unit_to = input("What is the unit you want to convert into?: ").strip().lower()

delete_last_lines(19)

if unit_from == unit_to:
    print(":^(")
else:
    measure = float(input(f"How many {unit_from}s are you converting?: "))
    if conversion_type == "weight":
        conversion_key = f"{unit_from}-{unit_to}"
        if conversion_key in conversion_factors:
            result = round_up(measure * conversion_factors[unit_from][unit_to], 3)
            print(f"{measure} {unit_from}(s) is {result} {unit_to}(s).")
        else:
            print("Conversion not supported.")
    elif conversion_type == "length":
        conversion_key = f"{unit_from}-{unit_to}"
        if conversion_key in conversion_factors:
            result = round_up(measure * conversion_factors[unit_from][unit_to], 3)
            print(f"{measure} {unit_from}(s) is {result} {unit_to}(s).")
        else:
            print("Conversion not supported.")
    else:
        print("Invalid conversion type.")
