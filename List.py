import copy
############### List Slicing in Python #############################################

# List slicing allows you to access a subset (slice) of a list using the syntax:
#   list[start:stop:step]
# - start: index to begin the slice (inclusive, default 0)
# - stop: index to end the slice (actually it takes end-1 i.e (start,end-1))(exclusive, default end of list)
# - step: interval between elements (default 1)
#
# Examples:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
print("numbers[2:5] =", numbers[2:5])  # [2, 3, 4]

# Omitting start (defaults to 0)
print("numbers[:4] =", numbers[:4])    # [0, 1, 2, 3]

# Omitting stop (defaults to end)
print("numbers[6:] =", numbers[6:])    # [6, 7, 8, 9]

# Using step
print("numbers[1:8:2] =", numbers[1:8:2])  # [1, 3, 5, 7]

# Negative indices
print("numbers[-3:] =", numbers[-3:])  # [7, 8, 9]

# Reversing a list
print("numbers[::-1] =", numbers[::-1])  # [9, 8, 7, ..., 0]

############### List Membership in Python #############################################

# You can check if an element exists in a list using the 'in' and 'not in' operators.
# These return True or False.
#
# Examples:
print("\nList Membership Examples:")
print("3 in numbers:", 3 in numbers)        # True
print("10 in numbers:", 10 in numbers)      # False
print("5 not in numbers:", 5 not in numbers)  # False

# Accessing both index and value in a list by enumerate()
print("\nAccessing both index and value in a list:")
my_list = ['a', 'b', 'c']
for index, value in enumerate(my_list):
	print(f"Index: {index}, Value: {value}")
print("15 not in numbers:", 15 not in numbers) # True

# Accessing both index and value in a list By zip():
my_list = ['a', 'b', 'c']
for index, value in zip(range(len(my_list)), my_list):
    print(f"Index: {index}, Value: {value}")

############### Common List Methods in Python #######################################
# Below are some of the most commonly used list methods, with definitions, examples, and expected outputs.

# 1. append(x): Adds an item x to the end of the list.
fruits = ['apple', 'banana']
fruits.append('cherry')
print("append example:", fruits)  # Expected output: ['apple', 'banana', 'cherry']

# 2. extend(iterable): Adds all elements of an iterable to the end of the list.
fruits.extend(['date', 'elderberry'])
print("extend example:", fruits)  # Expected output: ['apple', 'banana', 'cherry', 'date', 'elderberry']

# 3. insert(i, x): Inserts an item x at a given position i.
fruits.insert(1, 'blueberry')
print("insert example:", fruits)  # Expected output: ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

# 4. remove(x): Removes the first occurrence of x from the list.
fruits.remove('banana')
print("remove example:", fruits)  # Expected output: ['apple', 'blueberry', 'cherry', 'date', 'elderberry']

# 5. pop([i]): Removes and returns the item at position i (default last item).
last = fruits.pop()
print("pop example:", fruits)      # Expected output: ['apple', 'blueberry', 'cherry', 'date']
print("popped item:", last)        # Expected output: elderberry

# 6. index(x): Returns the index of the first occurrence of x.
idx = fruits.index('cherry')
print("index example:", idx)       # Expected output: 2

# 7. count(x): Returns the number of times x appears in the list.
count = fruits.count('apple')
print("count example:", count)     # Expected output: 1

# 8. sort(): Sorts the list in ascending order. ( modify the original list )
numbers2 = [3, 1, 4, 1, 5, 9]
numbers2.sort()
numbers2_desc = [3, 1, 4, 1, 5, 9]
numbers2_desc.sort(reverse=True)
print("sort descending example:", numbers2_desc)  # Expected output: [9, 5, 4, 3, 1, 1]
print("sort example:", numbers2)   # Expected output: [1, 1, 3, 4, 5, 9]

# 9. reverse(): Reverses the elements of the list in place.
numbers2.reverse()
print("reverse example:", numbers2) # Expected output: [9, 5, 4, 3, 1, 1]

# 10. copy(): Returns a shallow copy of the list.
copy_fruits = fruits.copy()
print("copy example:", copy_fruits) # Expected output: ['apple', 'blueberry', 'cherry', 'date']

# 11. clear(): Removes all items from the list.
copy_fruits.clear()
print("clear example:", copy_fruits) # Expected output: []

# 12. sorted(): Returns a new sorted list from the elements of any iterable (does not modify the original list).
numbers3 = [8, 2, 7, 3, 1]

sorted_numbers = sorted(numbers3)
sorted_numbers_desc = sorted(numbers3, reverse=True)
print("sorted example (ascending):", sorted_numbers)      # Expected output: [1, 2, 3, 7, 8]
print("sorted example (descending):", sorted_numbers_desc) # Expected output: [8, 7, 3, 2, 1]
print("original list remains unchanged:", numbers3)        # Expected output: [8, 2, 7, 3, 1]

# 13. split(): Although not a list method, split() is a string method that returns a list of substrings.
# It splits a string into a list using a specified separator (default is any whitespace).
text = "apple,banana,cherry"
split_list = text.split(",")
print("split example:", split_list)  # Expected output: ['apple', 'banana', 'cherry']


################# Shallow Copy vs Deep Copy ###################################################################################
#
# Shallow Copy:
# - A shallow copy creates a new list object, but does not create copies of the objects inside the list.
# - If the list contains mutable objects (like other lists), both the original and the copy will reference the same inner objects.
# - So both lists will reflect changes made to these inner objects.
# Example:
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0][0] = 99
print("shallow copy example:", shallow)   # Expected output: [[99, 2], [3, 4]]
print("original after shallow copy change:", nested) # Expected output: [[99, 2], [3, 4]]
a=[1,2,3,4,5,6]
b=a
a.pop()
print("deep copy example:", a)  # Expected output: [1, 2, 3, 4, 5]
print("original after deep copy change:", b)  # Expected output: [1, 2, 3, 4, 5]



# Deep Copy:
# - A deep copy creates a new list and recursively copies all objects inside the list.
# - Changes to the deep copy do not affect the original list, even for nested objects.
# - so both lists will not reflect changes made to these inner objects.
# Example:
deep = copy.deepcopy(nested)
deep[0][0] = 42
print("deep copy example:", deep)          # Expected output: [[42, 2], [3, 4]]
print("original after deep copy change:", nested)    # Expected output: [[99, 2], [3, 4]]
a=[1,2,3,4,5,6]
b=a[1:4]
print("deep copy example:", a)  # Expected output: [1, 2, 3, 4, 5, 6]
print("original after deep copy change:", b)  # Expected output: [2, 3, 4]


