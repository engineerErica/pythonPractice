# Week 7: (Lab Day) Data Structures in Python

""" In Class Task
For this session we'll build upon what we've done for the last few sessions and work on
Leetcode-style questions on your own. We'll go through the solutions toghether at the end.

"""
#UNFINISHED
"""
PROBLEM 1: Move Zeros
https://leetcode.com/problems/move-zeroes/description/ 
"""

"""
PROBLEM 2: Majority Element
https://leetcode.com/problems/majority-element/description/ 

"""

""" Post Class Task
PROBLEM 1: Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
"""
"""
1. Create a list/stack and a dictionary to match the brackets
2. Iterate through the string
    3. Check if the characters are not a pair: return false
    4. Else add the open bracket to the list
5. Check if the length of the stack is 0
    6. If yes return true, else return false

"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_stack = []
        my_dict = {"]": "[", ")": "(", "}": "{"}
        for char in s:
            if char in my_dict and len(my_stack) > 0:
                last_value = my_stack.pop()
                if my_dict[char] != last_value:
                    return False
            else:
                my_stack.append(char)
        if len(my_stack) == 0:
            return True
        else:
            return False

#UNFINISHED
"""
PROBLEM 2 (extra practice): Majority Element
https://leetcode.com/problems/majority-element/description/ 


"""

"""
PROBLEM 3 (extra practice): Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/description/ 

"""