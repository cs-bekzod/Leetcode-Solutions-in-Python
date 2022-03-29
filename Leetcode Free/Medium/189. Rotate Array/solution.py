# Problem Link: https://leetcode.com/problems/rotate-array

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        x = 5
        for i in range(k):
            nums.insert(0,nums[x])
            nums.pop()

print(Solution().rotate([1,2,3,4,5,6],6))


            
