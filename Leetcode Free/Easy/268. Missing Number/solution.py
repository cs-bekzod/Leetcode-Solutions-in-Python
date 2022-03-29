class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        maks = max(nums)
        MyList = [x for x in range(maks+1)]
        for i in MyList:
            if i not in nums:
                return i
        return maks+1