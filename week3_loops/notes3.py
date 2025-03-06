"""
Guide to Writing Loops in Python

*** for loops ***

You write a for loop for iterating over a sequence/iterable object.
Here's an example of how a simple for loop is done.

--------

for element in iterable:
    # Code to execute for each element

--------    

In the above case, the variable "element" represents a single variale in the "iterable" object.
The for loop will exit once all items in the iterable have been processed.
An example of an iterable is a string or a list.

Below are some code examples you can execute with. Feel free to comment out the examples and edit
the ones you want to play around with
"""
print("\nFOR LOOPS\n")
# Example: Iterating over a string
for letter in "banana":
    print(letter)

print() # Empty line

# Example: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print()

# Example: Using the range() function, which produces a sequence of integers from start (inclusive) to end (exclusive)
for i in range(1, 6):
    print(i) # This will print 1, 2, 3, 4, 5

x = [1,2,3,4,5]
idx = 0
for i in x:
    print(i)
    print("BRACKET NOTATION" , x[idx])
    idx += 1
"""
********************************

*** while loops ***

You write a while loop for iterating until a condition is False. The while loop will only begin when that codition is True.
Here's an example of how a simple for loop is done:

------------

while condition:
    # Code to execute for each element

------------    

In the above case, the variable "condition" is a condition that is set to either be "True" or "False".
The while loop will only begin to execute if that condition is "True". 
The while loop will stop executing once that condition is "False". 
It's important to ensure within the while loop you have logic that will eventually stop the while loop 
and ensure the condition is False. Or else the loop will continue forever. 

Below are some code examples you can execute with.
"""
print("\nWHILE LOOPS\n")


# Example: Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1 # Ensure the count is going up so the while loop will eventually stop

print()

num = 5
while num > 0:
    print(num)
    num -= 1  # Decrease num by 1 each time

"""
*********************
break & continue statements

You can incorporate these statements within the logic of your loops 

🔹 break → Exits the loop early
🔹 continue → Skips the current iteration and moves to the next

Below are some examples using break/continue
"""

print("\nBREAK & CONTINUE STATEMENTS\n")
# Example: Using break to exit a loop
i = 0
while i < 10:
    print(i)
    if i == 5:
        break
    i += 1

print()
# Example: Using "continue" to skip an iteration
for i in range(1, 6):
    if i == 3:
        continue
    print(i)


"""
*********************
Nested loops

You can nest loops inside each other. Here are some more examples:
"""
print("\nNESTED LOOPS\n")
# 3. Nested Loops
# You can nest loops inside each other.

# Example: Nested for loop
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")

print()
# Example: Nested while loop
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(f"i: {i}, j: {j}")
        j += 1
    i += 1