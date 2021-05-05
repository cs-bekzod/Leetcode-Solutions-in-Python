# Problem Link: https://leetcode.com/problems/remove-element/submissions/

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for j in nums:
            if j != val:
                nums[i] = j # <= ?
                i += 1
        return i
