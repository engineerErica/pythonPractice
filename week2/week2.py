# Guide to Python Data Types and Conditional Statements

# Integers
# Integers are whole numbers, positive or negative, without decimals.
a = 10
b = -5
print("Integer a:", a)
print("Integer b:", b)

# Floats
# Floats are numbers that contain a decimal point.
c = 10.5
d = -5.75
print("Float c:", c)
print("Float d:", d)

# type() function
# You can use the type() function to check the data type of a variable.
print("Type of a:", type(a))
print("Type of c:", type(a + c))

# Strings
# Strings are sequences of characters enclosed in quotes.
e = "Hello, World!"
f = 'Python is fun!'
print("String e:", e)
print("String f:", f)

# Conditional Statements
# Conditional statements allow you to execute certain code based on conditions.

# if statement
if a > 0:
    print("a is positive")

# if-else statement
if b > 0:
    print("b is positive")
else:
    print("b is not positive")

# if-elif-else statement
if c > 0:
    print("c is positive")
elif c == 0:
    print("c is zero")
else:
    print("c is negative")

# Nested if statements
if e == "Hello, World!":
    if f == 'Python is fun!':
        print("Both strings are as expected")

# Combining conditions with logical operators
if a > 0 and c > 0:
    print("Both a and c are positive")

if b < 0 or d < 0:
    print("At least one of b or d is negative")



'''IN CLASS TASK
Determine if a year is a leap year (divisible by 4 but not by 100 unless also divisible by 400)

Note: Make sure it's a number is inputted and not a string. 
We will go over error handling in a future class.
'''

print("Input a number: ")
a = int(input()) # input() returns a string even if a number is put in, so we convert it to an integer using int()
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
  print("Leap Year")
else:
  print("Not a leap year")

'''POST CLASS TASK
Write a Python program that asks the user for a single number and categorizes it based on specific conditions:

If the number is divisible by 3, print "Divisible by 3".
If the number is divisible by 5, print "Divisible by 5".
If the number is divisible by both 3 and 5, print "Divisible by both 3 and 5".
Otherwise, print "Not divisible by 3 or 5".

'''

print("Input a number: ")
a = int(input())
if a % 3 == 0 and a % 5 == 0:
    print("Divisible by both 3 and 5")
elif a % 3 == 0:
    print("Divisible by 3")
elif a % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")
