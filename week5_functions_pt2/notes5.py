# Guide to Writing Functions in Python Part 2
'''
WHAT ARE ARBITRARY ARGUMENTS (*args)? 
Arbitrary arguments allow you to pass an unknown number 
of non-keyword arguments to a function. 
This is useful when you don't know in advance how many 
arguments will be passed to your function.

When you use the "args" variable in the function, it's a tuple. You can't re-assign the values in the 
tuple, but you can iterate through them, similar to a list.

'''

'''Examples of arbitrary arguments (*args)'''
print("\nARBITRARY ARGUMENTS:")

def print_all_numbers(*numbers) -> None:
    # Let's use an example where were simply iterating and printing the values in "numbers"
    for i in numbers:
        print(i)
    return 

print("print_all_numbers():")
print_all_numbers(10, 9, 8, 7, 6, 5)
print()


def add_all_numbers(*numbers) -> int:
    total = 0
    for num in numbers:
        total = total + num
    return total

print("add_all_numbers", add_all_numbers(1,2,3.3))
print()


def greet_all_students(*students) -> str:
    all_students = ", ".join(students)
    return f"Hello {all_students}"

print(greet_all_students("Alice", "Alex", "Mark", "Magan"))
print()


'''
WHAT ARE ARBITRARY KEYWORD ARGUMENTS (**kwargs)? 
Arbitrary keyword arguments allow you to pass a variable number of keyword arguments to a function. 
This is useful when you want to handle named arguments that you don't know in advance.
This is the keyword equivalent to (*args).

Note, for keyword arguments, you need to have 2 stars (**).

When you use the keyword argument in the function, they're very similar to dictionaries (dict). The key is the keyword, and the value
is the value assined to the keyword.

For example, let's give this function:

def greet_students(**students):
    # ... Define the function....

And you call it like this: greet_students(first_name="Alice", last_name="Brown")....

When you use them within the function, the variable students will be a dict, represented like:
{
    first_name: "Alice",
    last_name: "Brown",
}

Let's use this as an example:
'''
'''Examples of arbitrary keyword arguments (*kwargs)'''
print("\nARBITRARY KEYWORD ARGUMENTS:")
def greet_students_with_kwargs_print_keys_and_values(**students) -> None:
    # Let's print out the keys and values in the dictionary to show we can use them in the function

    # We can iterate through a dictionary in Python like this:
    for key, value in students.items(): 
        print(key + ":", value)
    return 

greet_students_with_kwargs_print_keys_and_values(first_student="Alice", second_student="Magan", third_student="Annette")
print()



def greet_student_with_first_name_only(**kwargs) -> str:
    # In this example we're leveraging if a specific key exists. If not, print something else
    if "first_name" in kwargs:  # Check if 'name' key is in kwargs
        return f"Hello, {kwargs['first_name']}!"
    else:
        return "Hello, person without a first name!"

print(greet_student_with_first_name_only(first_name="Alice")) 
print()
print(greet_student_with_first_name_only(last_name="Brown"))
print()
print(greet_student_with_first_name_only(first_name="Alice", last_name="Brown"))
print()



"""
WHAT ARE LAMBDA FUNCTIONS?

Lambda functions are anonymous functions with the "lambda" keyword. 

They're a way to create simple functions without the need for a formal def statement and a function name.  

Think of them as "throwaway" functions you can define inline where you need them.

Lambda functions are usually small, and can only handle one expression. Anything bigger and it'd warrant a full function definition.

Here's the Python syntax:

---

lambda arguments: expression

---

lambda: The keyword that signifies a lambda function.
arguments: A comma-separated list of input arguments (can be zero or more).
expression: The single expression that is evaluated and returned.

"""
'''Examples of lambda functions'''
print("\nLAMBDA FUNCTIONS:")
square = lambda x: x ** 2
print(square(5))  # Output: 25


add = lambda x, y: x + y
result = add(5, 3)  # result will be 8
print(result)


greet_with_lambda = lambda name: "Hello, " + name + "!"
message = greet_with_lambda("Alice") 
print(message)
