############### Sets in Python #############################################

''' A set is an unordered collection of unique, immutable elements.
 Sets are useful for membership testing, removing duplicates, and performing mathematical set operations.'''

# Creating a set:
set1 = {1, 2, 3, 4}
print("set1:", set1)  # Output: {1, 2, 3, 4}

# Creating a set from a list (removes duplicates):
set2 = set([1, 2, 2, 3, 4, 4])
print("set2:", set2)  # Output: {1, 2, 3, 4}

# Empty set (must use set(), not {}):
empty_set = set()
print("empty_set:", empty_set)  # Output: set()

# Membership test:
print("2 in set1:", 2 in set1)  # Output: True
print("5 in set1:", 5 in set1)  # Output: False

# Sets are unordered, so indexing and slicing are not supported.

# Example of automatic duplicate removal:
set3 = {1, 2, 2, 3}
print("set3 (duplicates removed):", set3)  # Output: {1, 2, 3}

############### Common Set Methods in Python #############################################
# 1. add(x): Adds an element x to the set.
s = {1, 2, 3}
s.add(4)
print("add example:", s)  # Expected output: {1, 2, 3, 4}

# 2. update(iterable): Adds all elements from the iterable to the set.
s.update([5, 6])
print("update example:", s)  # Expected output: {1, 2, 3, 4, 5, 6}

# 3. remove(x): Removes x from the set. Raises KeyError if not found.
s.remove(6)
print("remove example:", s)  # Expected output: {1, 2, 3, 4, 5}

# 4. discard(x): Removes x if present. Does nothing if not found.
s.discard(10)
print("discard example:", s)  # Expected output: {1, 2, 3, 4, 5}

# 5. pop(): Removes and returns an arbitrary element from the set.
popped = s.pop()
print("pop example:", s)
print("popped element:", popped)

# 6. clear(): Removes all elements from the set.
s.clear()
print("clear example:", s)  # Expected output: set()

# 7. copy(): Returns a shallow copy of the set.
set_a = {1, 2, 3}
set_b = set_a.copy()
print("copy example:", set_b)  # Expected output: {1, 2, 3}

# 8. union(*others): Returns a new set with elements from the set and all others.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("union example:", set1.union(set2))  # Expected output: {1, 2, 3, 4, 5}

# 9. intersection(*others): Returns a new set with elements common to the set and all others.
print("intersection example:", set1.intersection(set2))  # Expected output: {3}

# 10. difference(*others): Returns a new set with elements in the set that are not in the others.
print("difference example:", set1.difference(set2))  # Expected output: {1, 2}

# 11. symmetric_difference(other): Returns a new set with elements in either set, but not both.
print("symmetric_difference example:", set1.symmetric_difference(set2))  # Expected output: {1, 2, 4, 5}

# 12. issubset(other): Checks if set is a subset of other.
print("issubset example:", {1, 2}.issubset(set1))  # Expected output: True

# 13. issuperset(other): Checks if set is a superset of other.
print("issuperset example:", set1.issuperset({1, 2}))  # Expected output: True

# 14. isdisjoint(other): Checks if sets have no elements in common.
print("isdisjoint example:", set1.isdisjoint({6, 7}))  # Expected output: True
