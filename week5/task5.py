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