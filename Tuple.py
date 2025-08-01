################# Different Ways to Define a Tuple in Python #############################################

# 1. Using parentheses
tuple1 = (1, 2, 3)
print("tuple1:", tuple1)  # Expected output: (1, 2, 3)

# 2. Without parentheses (comma-separated values)
tuple2 = 4, 5, 6
print("tuple2:", tuple2)  # Expected output: (4, 5, 6)

# 3. Single element tuple (must include a trailing comma)
tuple3 = (7,)
print("tuple3:", tuple3)  # Expected output: (7,)
tuple4 = 8,
print("tuple4:", tuple4)  # Expected output: (8,)

# 4. Using the tuple() constructor
tuple5 = tuple([9, 10, 11])
print("tuple5:", tuple5)  # Expected output: (9, 10, 11)

# 5. Empty tuple
empty_tuple1 = ()
empty_tuple2 = tuple()
print("empty_tuple1:", empty_tuple1)  # Expected output: ()
print("empty_tuple2:", empty_tuple2)  # Expected output: ()

################# Tuple Slicing in Python #############################################
# Tuple slicing allows you to access a subset (slice) of a tuple using the syntax:
#   tuple[start:stop:step]
# - start: index to begin the slice (inclusive, default 0)
# - stop: index to end the slice (exclusive, default end of tuple)
# - step: interval between elements (default 1)
#
# Examples:
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Basic slicing
print("numbers[2:5] =", numbers[2:5])  # (2, 3, 4)

# Omitting start (defaults to 0)
print("numbers[:4] =", numbers[:4])    # (0, 1, 2, 3)

# Omitting stop (defaults to end)
print("numbers[6:] =", numbers[6:])    # (6, 7, 8, 9)

# Using step
print("numbers[1:8:2] =", numbers[1:8:2])  # (1, 3, 5, 7)

# Negative indices
print("numbers[-3:] =", numbers[-3:])  # (7, 8, 9)

# Reversing a tuple
print("numbers[::-1] =", numbers[::-1])  # (9, 8, 7, ..., 0)

################# Arithmetic Operations on Tuples #############################################
# Tuples support some arithmetic operations using built-in operators:
#
# 1. Concatenation (+): Combines two tuples into one.
tuple_a = (1, 2, 3)
tuple_b = (4, 5)
result_concat = tuple_a + tuple_b
print("Concatenation:", result_concat)  # Expected output: (1, 2, 3, 4, 5)

# 2. Repetition (*): Repeats the tuple a specified number of times.
result_repeat = tuple_a * 3
print("Repetition:", result_repeat)  # Expected output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Note: Tuples do not support element-wise arithmetic (like addition or multiplication of corresponding elements) directly.
# For element-wise operations, you can use a comprehension or convert to a list or use numpy arrays.

# Example of element-wise addition using a comprehension:
tuple_x = (1, 2, 3)
tuple_y = (4, 5, 6)
result_elementwise = tuple(x + y for x, y in zip(tuple_x, tuple_y))
print("Element-wise addition:", result_elementwise)  # Expected output: (5, 7, 9)

# Built-in functions with tuples:
tuple_nums = (10, 20, 5, 8)
print("sum(tuple_nums):", sum(tuple_nums))    # Expected output: 43
print("min(tuple_nums):", min(tuple_nums))    # Expected output: 5
print("max(tuple_nums):", max(tuple_nums))    # Expected output: 20
print("len(tuple_nums):", len(tuple_nums))    # Expected output: 4

################# Tuple Sorting in Python #############################################
# Tuples are immutable, so they do not have a sort() method.
# However, you can use the built-in sorted() function to return a new sorted list from the elements of a tuple.
# If you need the result as a tuple, you can convert the list back to a tuple using tuple().
#
# Example:
unsorted_tuple = (5, 2, 8, 1)
sorted_list = sorted(unsorted_tuple)
print("sorted_list:", sorted_list)  # Expected output: [1, 2, 5, 8]
sorted_tuple = tuple(sorted_list)
print("sorted_tuple:", sorted_tuple)  # Expected output: (1, 2, 5, 8)
#
# For descending order:
sorted_tuple_desc = tuple(sorted(unsorted_tuple, reverse=True))
print("sorted_tuple (descending):", sorted_tuple_desc)  # Expected output: (8, 5, 2, 1)



