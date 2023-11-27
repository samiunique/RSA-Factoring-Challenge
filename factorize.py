import sympy

# Read numbers from the file
with open('tests/test00', 'r') as file:
    numbers = [int(line.strip()) for line in file]

# Factorize and print in the desired format
for num in numbers:
    factors = sympy.factorint(num)
    factors_str = '*'.join([f'{k}' for k in factors.keys()])
    print(f'{num}={factors_str}')

