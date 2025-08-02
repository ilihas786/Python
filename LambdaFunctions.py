# Lambda Functions in Python

# A lambda function is a small anonymous function defined with the lambda keyword.
# Syntax: lambda arguments: expression
# Lambda functions can have any number of arguments but only one expression.
# They are often used for short, simple functions, especially as arguments to higher-order functions like map(), filter(), and sorted().

# Example 1: Add 10 to a number
x = lambda x: x + 10
print(x(10))  # Output: 20

# Example 2: Multiply two numbers
multiply = lambda a, b: a * b
print(multiply(3, 4))  # Output: 12

# Example 3: Use with map()
nums = [1, 2, 3, 4]
result = list(map(lambda n: n * n, nums))
print('Squares:', result)  # Output: [1, 4, 9, 16]

# Example 4: Use with filter()
evens = list(filter(lambda n: n % 2 == 0, nums))
print('Evens:', evens)  # Output: [2, 4]

check_even_odd_lambda = lambda x:x%2 == 0
print("Is 4 even?", check_even_odd_lambda(4)) 

sum = lambda a,b :a+b
print("Sum of 5 and 3:", sum(5, 3))  # Output: 8