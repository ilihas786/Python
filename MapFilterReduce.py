''' MAP FUNCTION EXAMPLE '''

radii=[2,3,4,5,6,7]
print(map(lambda x:x**2, radii))  # This will return a map object, not the actual list 
print(list(map(lambda x:x**2, radii)))  # This will return the actual list , please remember toconvert map object to a list

# Looping directly over map object
for value in map(lambda x: x**2, radii):
    print(value)

data = [('Mumbai', 32), ('Delhi', 45), ('Bangalore', 30), ('Chennai', 40)]
# Use Formula for Conversion: F = C * 9/5 + 32
cel_to_fahrenheit = lambda element : (element[0],(9/5) * element[1] + 32)
x=list(map(cel_to_fahrenheit,data))
print(x)

''' FILTER FUNCTION EXAMPLE '''

data=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x:x%2==0,data)))  # This will return a list of even numbers

# Looping directly over filter object
for value in filter(lambda x:x%2==0,data):
    print(value)

# It is not necessary to convert it into list we can convert it into a tuple or set as well

# FILTER FUNCTION TO REMOVE NULL (FALSY) VALUES
# In Python, the following are treated as null (falsy): None, False, 0, 0.0, '', [], {}, set(), etc.
# filter(None, iterable) removes all falsy values from the iterable.
data_with_nulls = [0, 1, '', None, 2, False, 3, [], {}, 4]
filtered = list(filter(None, data_with_nulls))
print('After filtering null (falsy) values:', filtered)  # Expected output: [1, 2, 3, 4]

''' REDUCE FUNCTION EXAMPLE '''
# The reduce() function applies a rolling computation to sequential pairs of values in a list (or any iterable), reducing it to a single value.
# It is available in the functools module.
from functools import reduce
# syntax: reduce(function, iterable)
# Example: Sum all numbers in a list
nums = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, nums)
print('Sum using reduce:', total)  # Expected output: 15

# Example: Find the maximum value in a list
max_value = reduce(lambda x, y: x if x > y else y, nums)
print('Max using reduce:', max_value)  # Expected output: 5
