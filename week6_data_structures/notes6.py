# Week 6: Data Structures in Python

"""
LISTS

Lists are versatile and mutable (changeable) ordered sequence of items.  
Think of it like a container that can hold various types of data, and you can 
access those items by their position (index).

Lists are indexed - the position of each item is significant. You can fetch a specific value 
from a list based off the index.

Lists are dynamic - they can be added

You can also store different data types (e.g. str, int) within the same list.

You represent lists using square brackets [] and separate items with commas.
Here's the example syntax:

my_list = [1, 2, "hello", 3.14, True]  # Mixed data types
empty_list = []  # An empty list

Note: The word "list" and "array" are used interchangably. However there is a difference in Python.
You should almost always use a list, as described in this class. Arrays are technically different,
which uses the array.arrays module, which is not mutable and optimized for memory efficiency.

Useful list operations:
    .index(item): Returns the index of the first occurrence of an item.
    .count(item): Returns the number of times an item appears in the list.
    .sort(): Sorts the list in place 
    .reverse(): Reverses the order of the items in place.
    .copy(): Creates a shallow copy of the list
    len(my_list): Returns the number of elements in the variable my_list

"""

fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Accessing elements via index
print(fruits[0])  # Output: apple

# Adding elements using .append()
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Removing elements .remove()
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']

# You can remove by index via .pop(index), or .pop() for the last element
fruits.pop(1)
print(fruits)  # Output: ['apple', 'orange']

fruits.pop()
print(fruits)  # Output: ['apple']

# You can also get parts of an array (slicing)
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # Output: [20, 30, 40] (items from index 1 up to, but not including, index 4)
print(my_list[:3])   # Output: [10, 20, 30] (from the beginning up to index 3)
print(my_list[2:])   # Output: [30, 40, 50] (from index 2 to the end)


"""
TUPLES

Tuples in Python is an ordered, immutable sequence of items.  
Think of it like a read-only list. Once you create a tuple, you cannot change 
its contents (add, remove, or modify elements). This immutability is the key difference between tuples and lists.

They are useful when you need to store a collection of items that should not be changed.

You represent tuples using parantheses () and separate items with commas.
Here's the example syntax:

my_tuple = (1, 2, "hello", 3.14, True)  # Mixed data types
empty_tuple = ()  # An empty tuple

Many of the operations (getting length, slicing, etc.) are the same as lists
"""

coordinates = (10, 20)
print(coordinates)  # Output: (10, 20)

# Accessing elements
print(coordinates[1])  # Output: 20

# Slicing
my_tuple = (10, 20, 30, 40, 50)
print(my_tuple[1:4])  # Output: (20, 30, 40)

"""
SETS

Sets are unordered collections of unique items. They are useful when you need to store multiple items and ensure that each item is unique.

Key characteristics of sets:
- Unordered: The items in a set do not have a defined order.
- Unique: Each item in a set must be unique. Duplicate items are automatically removed.
- Mutable: You can add or remove items from a set.

You represent sets using curly braces {} or the set() function. Here's the example syntax:

my_set = {1, 2, 3, 4, 5}  # A set with unique integers
empty_set = set()  # An empty set

Note: You cannot create an empty set using {} because it creates an empty dictionary. Always use the set() function for an empty set.

Useful set operations:
    .add(item): Adds an item to the set.
    .remove(item): Removes an item from the set. Raises a KeyError if the item is not found.
    .discard(item): Removes an item from the set if it is present. Does nothing if the item is not found.
    .union(other_set): Returns a new set with all items from both sets.
    .intersection(other_set): Returns a new set with only the items that are present in both sets.
    .difference(other_set): Returns a new set with items that are in the first set but not in the second set.
    .symmetric_difference(other_set): Returns a new set with items that are in either set, but not in both.

Example:
my_set = {1, 2, 3}
my_set.add(4)  # my_set is now {1, 2, 3, 4}
my_set.remove(2)  # my_set is now {1, 3, 4}
my_set.union({5, 6})  # Returns {1, 3, 4, 5, 6}
"""
unique_numbers = {1, 2, 3, 4, 4, 5}
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}

# Adding elements
unique_numbers.add(6)
print(unique_numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
unique_numbers.remove(3)
print(unique_numbers)  # Output: {1, 2, 4, 5, 6}

# Check if a value is in a set
if 1 in unique_numbers:
    print("There's a 1 in unique_numbers")
else:
    print("There's no 1 in unique_numbers")

"""

DICTIONARIES

Dictionaries are mutable, unordered collections of key-value pairs. They are useful when you need to associate unique keys with specific values.

Key characteristics of dictionaries:
- Unordered: The items in a dictionary do not have a defined order.
- Key-value pairs: Each item in a dictionary consists of a key and a value. Keys must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any data type.
- Mutable: You can add, remove, or modify key-value pairs in a dictionary.

You represent dictionaries using curly braces {} with key-value pairs separated by colons. Here's the example syntax:

my_dict = {"name": "Alice", "age": 30, "is_student": False}  # A dictionary with string keys and mixed value types
empty_dict = {}  # An empty dictionary

Useful dictionary operations:
    .keys(): Returns a view object containing the dictionary's keys.
    .values(): Returns a view object containing the dictionary's values.
    .items(): Returns a view object containing the dictionary's key-value pairs.
    .get(key, default=None): Returns the value for the specified key. If the key is not found, returns the default value.
    .update(other_dict): Updates the dictionary with key-value pairs from another dictionary.
    .pop(key, default=None): Removes the specified key and returns its value. If the key is not found, returns the default value.

"""