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



