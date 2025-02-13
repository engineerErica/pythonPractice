"""
TASK #1A
Write a function that takes in a temperature Fahrenheit and returns it's equivalent in Celsius. 

Formula: °C = (°F - 32) x (5/9)
"""
def fahrenheit_to_celsius(temperature):
    return (temperature - 32) * (5/9)

result1A = fahrenheit_to_celsius(32)
print(result1A == 0.0)

"""
TASK #1B
Write a function that takes in a temperature Celsius and returns it's equivalent in Kelvin. 

Formula: Kelvin = °C + 273.15
"""

def celsius_to_kelvin(temperature):
    return temperature + 273.15

result1B = celsius_to_kelvin(0)
print(result1B == 273.15)

"""
TASK #1C
Write a function that takes in a temperature Fahrenheit and returns it's equivalent in Kelvin. 
NOTE: You must only use the functions used in the first two tasks.
"""

def fahrenheit_to_kelvin(temperature):
    return celsius_to_kelvin(fahrenheit_to_celsius(temperature))

result1C = fahrenheit_to_kelvin(32)
print(result1C == 273.15)
# ---------------------------------------------------------------------------------------------------

"""
TASK #2
Write a function factorial(n) that returns the factorial of n.

Example: 5! = 5 x 4 x 3 x 2 x 1 = 120

Hint: The factorial of 0 or 1 equals 1. 0! = 1, 1! = 1.

"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    output = 1
    for num in range(n, 0, -1):
        output = num * output
    return output

result2 = factorial(5)
print(result2 == 120)

"""
NUMBER GUESSING GAME

Write a function that lets a user guess a number between 1 & 100. 
If their guess is too low, tell the user (i.e. print to the console) it's too low.
If their guess is too high, tell the user it's too high.
If their guess is correct, tell them it's correct and exit the function.

Use the function "random.randint(1, 100)" to generate a number between 1 and 100. 

Hint: Use "int(input())" to get an input from the user as an integer

"""

# This is an import for the Python Library "random". We will discuss more about imports later
import random 

# This is how you generate a random number between 1 & 100. Use this in your function
print(random.randint(1, 100))



# Write your function here....

def guess_number():
    random_num = random.randint(1, 100)
    while True:
        num = int(input("Input a number: "))
        if num < random_num:
            print("It's too low")
        elif num > random_num:
            print("It's too high")
        else:
            print("Correct!")
            return
guess_number()