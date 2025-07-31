############### Converting float string to int #############################################

float_str = "12.34"
float_value = float(float_str)
int_value = int(float_value)
print("Original string:", float_str)
print("As float:", float_value)
print("As int:", int_value)

# Example 2: Immutable String in Python

name = "Alice"
print("Original string:", name)

# Attempting to change a character (will raise an error)
try:
    name[0] = "M"
except TypeError as e:
    print("Error:", e)

# Strings are immutable, so to change them, you must create a new string
new_name = "M" + name[1:]
print("Modified string:", new_name)

##### Basic Operations in Python (with edge cases) #############################################

# Addition
a = 5
b = 3
print("Addition:", a, "+", b, "=", a + b)
# Expected output: Addition: 5 + 3 = 8

# Subtraction
print("Subtraction:", a, "-", b, "=", a - b)
# Expected output: Subtraction: 5 - 3 = 2

# Multiplication
print("Multiplication:", a, "*", b, "=", a * b)
# Expected output: Multiplication: 5 * 3 = 15
# Expected output: Division: 5 / 3 = 1.6666666666666667
#                  Error: division by zero

# Division (normal and edge case: division by zero)
try:
    print("Division:", a, "/", b, "=", a / b)
    print("Division by zero:", a, "/ 0 =", a / 0)
except ZeroDivisionError as e:
    print("Error:", e)

# Integer Division
print("Integer Division:", a, "//", b, "=", a // b)
# Expected output: Integer Division: 5 // 3 = 1

# Modulus
print("Modulus:", a, "%", b, "=", a % b)
# Expected output: Modulus: 5 % 3 = 2
# Expected output: Error: integer division or modulo by zero
try:
    print("Modulus by zero:", a, "% 0 =", a % 0)
except ZeroDivisionError as e:
    print("Error:", e)

# Exponentiation
print("Exponentiation:", a, "**", b, "=", a ** b)
# Expected output: Exponentiation: 5 ** 3 = 125

# Negative numbers
c = -2
print("Addition with negative:", a, "+", c, "=", a + c)
# Expected output: Addition with negative: 5 + -2 = 3

# Large numbers
large_num = 10**100
print("Large number addition:", large_num, "+ 1 =", large_num + 1)
# Expected output: Large number addition: 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 + 1 = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001

# Floating point precision
f1 = 0.1
f2 = 0.2
print("Floating point addition:", f1, "+", f2, "=", f1 + f2)
# Expected output: Floating point addition: 0.1 + 0.2 = 0.30000000000000004

    