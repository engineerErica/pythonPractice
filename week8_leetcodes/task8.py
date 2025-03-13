""" In Class Task
PROBLEM 1: Intersection of Two Arrays (Will go over this together)
https://leetcode.com/problems/intersection-of-two-arrays/

Brute Force Solution
1. initialize output list as well as a set to keep track of only unique overlaps
2. Iterate over nums1
    3. Iterate over nums2
        4. Check if the chars match and if the char is not in the set already
            5. If true, add the char to the set and list
        5. Else continue
6. Return the list
"""
#Problem 1 Brute force solution
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []
        my_set = set()
        for char1 in nums1:
            for char2 in nums2:
                if char1 == char2 and char1 not in my_set:
                    my_set.add(char1)
                    intersection.append(char1)
        return intersection

"""
Optimized Solution:
1. Initialize nums1 into a set
2. Initialize result set
3. Iterate over nums2
    4. If the val from nums2 is in the set, add it to the result
5. return the restult as a list
"""
#Problem 1 Optimized Solution
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set_nums1 = set(nums1)
        result = set()
        for num in nums2:
            if num in set_nums1:
                result.add(num)
        return list(result)

"""

PROBLEM 2: Two Sum
https://leetcode.com/problems/two-sum/description/

1. Initialize a dictionary and an index variable
2. Iterate over the list of nums
    3. Initialize a variable to store the value that combines with the curr num to reach the target
    4. if the supplemental value is a key in the dictionary, return the current index and the value at the key
    5. Else initialize the curr num as a key in the dict with the value as the index
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_dict = {}
        i = 0
        for num in nums:
            supplemental_val = target - num
            if supplemental_val in my_dict:
                return [my_dict[supplemental_val], i]
            else:
                my_dict[num] = i
            i += 1

""" UNFINISHED
Post Class Task:

PROBLEM: Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/description/

Hint: Use the sorted() funciton to sort a list in Python.
"""
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results = []
        right = len(nums) - 1
        left = 0

        while left <= right:
            if nums[left] ** 2 < nums[right] ** 2:
                results.append(nums[right] ** 2)
                right -= 1
            else:
                results.append(nums[left] ** 2)
                left += 1
                
        return results[::-1]

#time complexity for the above solution is linear because we only loop once

        # for i in range(0, len(nums)):
        #     nums[i] = nums[i] ** 2
        #     i+=1
        # return sorted(nums)
#time complexity of the above solution is o(nlog(n)) becuase its using the sorted