class Solution(object):
    def moveZeroes(self, nums):
        append_times=nums.count(0)
        for i in range(append_times):
            nums.remove(0)
            nums.append(0)
    