class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return len([x for x in nums if x < target])

