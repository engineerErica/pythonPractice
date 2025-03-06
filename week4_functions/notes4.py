# Guide to Writing Functions in Python

'''
WHAT ARE FUNCTIONS? 
A function is a reusable block of code that performs a specific task.
It helps in organizing code, reducing redundancy, and improving readability. 
Functions in Python are defined using the "def" keyword.
'''

'''
WHY USE FUNCTIONS?
- Code Reusability: Write once, use multiple times
- Modularity: Break down complex problems into smaller, manageable parts.
- Readability & Maintainability: Make the code more structured and easier to debug.
- Avoid Redundancy: Reduce duplication of code.
'''

'''
HOW TO DEFINE A FUNCTION?
A function is defined using the def keyword, followed by the function name and parentheses.
'''
print("\nDEFINING A FUNCTION EXAMPLES")
# Example: Basic function
def greet() -> None:
    print("Hello, world!")

# Calling the function
greet()


'''
FUNCTION ARGUMENTS
Functions can take arguments, which are specified within the parentheses.
A function doesn't need arguments, like in the greet() example above.
But in practice, functions usually have arguments.
You can consider these *positional* arguments, as the order of the arguments matters when you use them.
'''
print("\nFUNCTION ARGUMENTS EXAMPLES")

# Example: Function with arguments
def greet_person(name) -> None:
    print(f"Hello, {name}!")

# Calling the function with an argument
greet_person("Alice")

def greet_person_full_name(first_name, last_name) -> None:
    print(f"Hello, {first_name} {last_name}!")

# Calling the function with multiple arguments:
greet_person_full_name("Alice", "Brown")

'''
DEFAULT ARGUMENTS
You can provide default values for arguments. So if you call a function and don't input the argument,
then it'll use the default in execution.
'''
print("\nDEFAULT ARGUMENTS EXAMPLES")

# Example: Function with default argument
def greet_person(name="Guest") -> None:
    print(f"Hello, {name}!")

# Calling the function without an argument
greet_person()
# Calling the function with an argument
greet_person("Bob")    

'''
RETURN VALUES
Functions can return values using the "return" statement.
If no return statement is used, the function returns None by default.
'''
print("\nRETURN VALUES EXAMPLES")
# Functions can return values using the return statement.

# Example: Function that returns a value
def add(a, b) -> int:
    return a + b

# Calling the function and storing the result
result = add(3, 5)
print(result)


'''
KEYWORD ARGUMENTS
You can call functions using keyword arguments.
Use keyword arguments for better readability and flexibility
'''
print("\nKEYWORD ARGUMENTS")
# Example: A basic function definition
def describe_person(name, age) -> None:
    print(f"{name} is {age} years old.")

# Example calling the function with keyword arguments
# Notice the order of how you call the values don't matter when you invoke the keyword args
# Keyword arguments are usually better as it makes code more clear
describe_person(age=30, name="Charlie")

# Below is an example of the same function but using positional arguments. 
describe_person("Charlie", 30)