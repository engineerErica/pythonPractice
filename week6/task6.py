"""
TASK 1 - REMOVE DUPLICATES

Given a list of numbers, remove duplicates while maintaining the order of the values. Return the updated list.

Example 1:

Input: nums = [1, 2, 2, 3, 4, 4, 5]  
Output: [1, 2, 3, 4, 5]


Example 2:

Input: nums = [25, 25, 30, 35, 40]
Output: [25, 30, 35, 40]

"""

def remove_duplicates(nums) -> list[int]:
    unique_nums = set()
    for num in nums:
        if num in unique_nums:
            nums.remove(num)
        else:
            unique_nums.add(num)
    return nums
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5])
print(remove_duplicates([25, 25, 30, 35, 40]) == [25, 30, 35, 40])


"""
TASK 2

Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

"""

"""
POST CLASS TASK - GROUP ANAGRAMS

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An anagram is a word/phrase formed by rearranging the letters of a different word/phrase, using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation: 
    "eat", "tea", and "ate" are anagrams.
    "tan" and "nat" are anagrams.
    "bat" has no anagrams.

Example 2: 
Input: strs = ["hello", "world", "python", "java"]
Output: [["hello"], ["world"], ["python"], ["java"]]

Explanation:
    None of these words are anagrams, so each remains in its own group.

    
Note: you can test/execute your code here: https://leetcode.com/problems/group-anagrams/description/

"""