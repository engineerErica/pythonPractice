"""
TASK 1:

Write a max_finder() function that takes in an unknown amount of numbers (using *args) and returns the maximum number.

"""
def max_finder(*numbers) -> int:
    max_num = numbers[0]
    for num in numbers:
        if max_num < num:
            max_num = num
    return max_num

print(max_finder(7, 15, 10, 2) == 15)

"""
TASK 2:

Write a lambda function that returns True if a number is even, otherwise return False

"""
isEvenOrOdd = lambda number: number % 2 == 0
print(isEvenOrOdd(50))

"""Post Class Task
PROFILE BUILDER

Create a function that builds a person's profile from keyword arguments.

Create a function "build_profile" that accepts any number of keyword arguments representing attributes of a person (e.g., name, age, city, occupation). 
The function should print the profile information in a formatted way.

Example usage:
build_profile(name="Alice", age=30, city="New York")
# Output:
# Name: Alice
# Age: 30
# City: New York


build_profile(name="Bob", occupation="Software Engineer")
# Output:
# Name: Bob
# Occupation: Software Engineer
 
"""
def build_profile(**profile_info) -> None:
    for key, value in profile_info.items():
        print(f"{key.capitalize()}: {value}")
    return
build_profile(name="Alice", age=30, city="New York")
build_profile(name="Bob", occupation="Software Engineer")
