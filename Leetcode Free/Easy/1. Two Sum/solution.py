# Problem Link: https://leetcode.com/problems/two-sum/
# Solution 1
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for x in range(len(nums)):
#             for y in range(1,len(nums)):
#                 if nums[x] + nums[y] == target and x != y:
#                     return [x,y]
