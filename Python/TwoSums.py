# created by ymirwani

# Problem:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Solution:
from typing import List

# 1. O(n) time complexity using a dictionary (hash table) to store the previously seen numbers
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create dictionary to store the value-to-index mapping
        num_dict = {}
        for i, num in enumerate(nums):
            # check if complement exists in dictionary 
            if target - num in num_dict: 
                return [num_dict[target - num], i]
            num_dict[num] = i
        return []

# 2. Brute force
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []  # No solution found

# 3. Two-pass hash table
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numMap = {}
#         n = len(nums)
#         # Build the hash table
#         for i in range(n):
#             numMap[nums[i]] = i
#         # Find the complement
#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap and numMap[complement] != i:
#                 return [i, numMap[complement]]
#         return []  # No solution found

# 4. One-pass hash table
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numMap = {}
#         n = len(nums)
#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap:
#                 return [numMap[complement], i]
#             numMap[nums[i]] = i
#         return []  # No solution found



if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert (Solution().twoSum(nums, target) == [0, 1])

    print(Solution().twoSum(nums, target))  # Output: [0, 1]
    
    nums = [3, 2, 4]
    target = 6
    assert (Solution().twoSum(nums, target) == [1, 2])

    # 1. Runtime 58 ms -> after 3 runs -> 57 ms
    # 2. Runtime 69 ms
    # 3. Runtime 88 ms
    # 4. Runtime 76 ms