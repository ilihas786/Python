###### Different Ways to Use Loops with Iterables in Python #####################

# 1. Looping through a list
fruits = ['apple', 'banana', 'cherry']
print('Looping through a list:')
for fruit in fruits:
    print(fruit)

# 2. Looping through a set
colors = {'red', 'green', 'blue'}
print('Looping through a set:')
for color in colors:
    print(color)

# 3. Looping through a tuple
numbers = (1, 2, 3)
print('Looping through a tuple:')
for num in numbers:
    print(num)

# 4. Looping through a string
text = 'hello'
print('Looping through a string:')
for char in text:
    print(char)

# 5. Looping through a dictionary (keys)
person = {'name': 'Alice', 'age': 30}
print('Looping through dictionary keys:')
for key in person:
    print(key)

# 6. Looping through dictionary values
print('Looping through dictionary values:')
for value in person.values():
    print(value)

# 7. Looping through dictionary items (key-value pairs)
print('Looping through dictionary items:')
for key, value in person.items():
    print(key, value)

# 8. Using enumerate() to get index and value
print('Using enumerate on a list:')
for idx, fruit in enumerate(fruits):
    print(idx, fruit)

# 9. Using range() to loop a specific number of times
print('Using range:')
for i in range(3):
    print(i)

# 10. List comprehension (compact loop)
squares = [x*x for x in range(5)]
print('List comprehension:', squares)

#################### Comprehensions in Python ####################

# Comprehensions provide a concise way to create lists, sets, or dictionaries from iterables.
# They can also be used to create generator expressions.
#
# 1. List Comprehension: [expression for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]
print('List comprehension (evens):', evens)  # [0, 2, 4, 6, 8]

# 2. Set Comprehension: {expression for item in iterable if condition}
unique_lengths = {len(word) for word in ['apple', 'banana', 'pear']}
print('Set comprehension:', unique_lengths)  # {4, 5, 6}

# 3. Dictionary Comprehension: {key_expr: value_expr for item in iterable if condition}
square_dict = {x: x*x for x in range(5)}
print('Dict comprehension:', square_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 4. Generator Expression: (expression for item in iterable if condition)
gen = (x*x for x in range(3))
print('Generator expression:', list(gen))  # [0, 1, 4]

# Comprehensions are often more readable and efficient than using loops to build new collections.


