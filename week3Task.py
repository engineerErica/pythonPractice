""" IN CLASS TASK
Write a Python program takes in a number, and prints the numbers from 1 to that given number, but:

For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
For multiples of both 3 and 5, print "FizzBuzz".

Here's an example output if you input the number 15: 

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz

"""

print("Input a number: ")
val = int(input())
for i in range(1, val + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: print(i)

i = 0
while i <= val:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else: 
        print(i)
    i+=1

"""POST CLASS TASK
Problem: Write a program to check if a given string is a palindrome. A palindrome reads the same backward as forward (e.g., "madam" or "racecar").

Given a string s, print True if it is a palindrome, or False otherwise.

Examples:
"abba" -> True
"racecar" --> True
"dad" -> True
"helloworld" -> False
"marcy" -> False

Note: Ignore edge cases with capital letters, punctuation characters, etc. for the purpose of this exercise.

Hints
    1. A string is an iterable object. For example if x = "hello", then x[0] equals "h", x[1] equals "e", x[2] equals "l", etc..
    2. You can get the length of a string by using the builtin function len() (ex: len(x))
    3. See if you can solve with a two-pointer approach.
"""

print("Input a string: ")
val = str(input())
startIdx = 0
endIdx = len(val) - 1
flag = True
while endIdx > startIdx:
    if val[startIdx] != val[endIdx]:
        print("False")
        flag = False
        break
    startIdx += 1
    endIdx -= 1
if flag:
    print(True)