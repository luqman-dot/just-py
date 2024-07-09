import math

def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

conversion_factors = {
    "pound": {"ounce": 16, "gram": 453.592, "milligram": 453592, "kilogram": 0.453592},
    "ounce": {"pound": 0.0625, "gram": 28.3495, "milligram": 28349.5, "kilogram": 0.0283495},
    "gram": {"pound": 0.00220462, "ounce": 0.035274, "milligram": 1000, "kilogram": 0.001},
    "milligram": {"pound": 2.20462e-6, "ounce": 3.5274e-5, "gram": 0.001, "kilogram": 1e-6},
    "kilogram": {"pound": 2.20462, "ounce": 35.274, "gram": 1000, "milligram": 1000000},
    "yard": {"foot": 3, "inch": 36, "meter": 0.9144, "centimeter": 91.44, "kilometer": 0.0009144, "mile": 0.000568182},
    "foot": {"yard": 0.333333, "inch": 12, "meter": 0.3048, "centimeter": 30.48, "kilometer": 0.0003048, "mile": 0.000189394},
    "inch": {"yard": 0.0277778, "foot": 0.0833333, "meter": 0.0254, "centimeter": 2.54, "kilometer": 2.54e-5, "mile": 1.57828e-5},
    "meter": {"yard": 1.09361, "foot": 3.28084, "inch": 39.3701, "centimeter": 100, "kilometer": 0.001, "mile": 0.000621371},
    "centimeter": {"yard": 0.0109361, "foot": 0.0328084, "inch": 0.393701, "meter": 0.01, "kilometer": 1e-5, "mile": 6.21371e-6},
    "kilometer": {"yard": 1093.61, "foot": 3280.84, "inch": 39370.1, "meter": 1000, "centimeter": 100000, "mile": 0.621371},
    "mile": {"yard": 1760, "foot": 5280, "inch": 63360, "meter": 1609.34, "centimeter": 160934, "kilometer": 1.60934}
}

def convert_units(amount, from_unit, to_unit):
    if from_unit in conversion_factors and to_unit in conversion_factors[from_unit]:
        return round_up(amount * conversion_factors[from_unit][to_unit], 3)
    else:
        return None

def print_options():
    print("Length Options: Yard, Foot, Inch, Meter, Centimeter, Kilometer, Mile")
    print("Weight Options: Pound, Gram, Milligram, Ounce, Kilogram")
    print()

print_options()

category = input("Would you like to convert weight or length?: ").strip().lower()
unit_from = input("What is your starting unit?: ").strip().lower()
unit_to = input("What is your target unit?: ").strip().lower()
amount = float(input(f"How many {unit_from}s are you converting?: ").strip())

result = convert_units(amount, unit_from, unit_to)

if result is not None:
    print(f"{amount} {unit_from}(s) is {result} {unit_to}(s).")
else:
    print("Conversion not possible. Please check your units.")