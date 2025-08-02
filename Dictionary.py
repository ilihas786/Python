########## Dictionaries in Python ############################################

# A dictionary is an unordered collection of key-value pairs.
# Keys must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any type.
# Dictionaries are useful for fast lookups, data organization, and mapping relationships.
#
# Creating a dictionary:
person = {"name": "Alice", "age": 30, "city": "New York"}
print("person:", person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Accessing values by key:
print("person['name']:", person["name"])  # Output: Alice

# Adding or updating a key-value pair:
person["email"] = "alice@example.com"
print("after adding email:", person)

# Removing a key-value pair:
del person["age"]
print("after deleting age:", person)

# Checking if a key exists:
print("'city' in person:", "city" in person)  # Output: True
print("'age' in person:", "age" in person)    # Output: False

# Dictionaries are unordered (before Python 3.7), but maintain insertion order in Python 3.7+.


########## Common Dictionary Methods in Python ############################################
# 1. get(key[, default]): Returns the value for key if key is in the dictionary, else default.
person = {"name": "Alice", "city": "New York", "email": "alice@example.com"}
print("get example:", person.get("name"))  # Expected output: Alice
print("get with default:", person.get("age", "Not found"))  # Expected output: Not found

# 2. keys(): Returns a view object of all keys.
print("keys example:", list(person.keys()))  # Expected output: ['name', 'city', 'email']

# 3. values(): Returns a view object of all values.
print("values example:", list(person.values()))  # Expected output: ['Alice', 'New York', 'alice@example.com']

# 4. items(): Returns a view object of all key-value pairs (as tuples).
print("items example:", list(person.items()))  # Expected output: [('name', 'Alice'), ('city', 'New York'), ('email', 'alice@example.com')]

# 5. pop(key[, default]): Removes specified key and returns the value. If key not found, returns default if given, else raises KeyError.
person2 = {"name": "Alice", "city": "New York", "email": "alice@example.com"}
email = person2.pop("email")
print("pop example:", email)  # Expected output: alice@example.com
print("after pop:", person2)

# 6. popitem(): Removes and returns the last inserted key-value pair as a tuple.
person3 = {"name": "Alice", "city": "New York"}
last_item = person3.popitem()
print("popitem example:", last_item)
print("after popitem:", person3)

# 7. update([other]): Updates the dictionary with key-value pairs from other, overwriting existing keys.
person4 = {"name": "Alice", "city": "New York"}
person4.update({"country": "USA", "city": "Boston"})
print("update example:", person4)  # Expected output: {'name': 'Alice', 'country': 'USA', 'city': 'Boston'}

# 8. clear(): Removes all items from the dictionary.
person5 = {"name": "Alice", "city": "New York"}
person5.clear()
print("clear example:", person5)  # Expected output: {}

# 9. copy(): Returns a shallow copy of the dictionary.
person6 = {"a": 1, "b": 2}
person6_copy = person6.copy()
print("copy example:", person6_copy)  # Expected output: {'a': 1, 'b': 2}


########## Different Ways to Iterate Over a Dictionary ############################################
sample_dict = {"a": 1, "b": 2, "c": 3}

# 1. Iterate over keys (default)
print("Iterate over keys:")
for key in sample_dict:
    print(key)

# 2. Iterate over keys explicitly
print("Iterate over keys (explicit):")
for key in sample_dict.keys():
    print(key)

# 3. Iterate over values
print("Iterate over values:")
for value in sample_dict.values():
    print(value)

# 4. Iterate over key-value pairs
print("Iterate over key-value pairs:")
for key, value in sample_dict.items():
    print(key, value)

# 5. Iterate with index using enumerate
print("Iterate with index:")
for idx, (key, value) in enumerate(sample_dict.items()):
    print(idx, key, value)
