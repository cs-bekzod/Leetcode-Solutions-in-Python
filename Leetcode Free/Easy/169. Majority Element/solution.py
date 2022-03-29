class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dictt = {}
        for i in nums:
            listt = dictt.keys()
            if i in listt:
                dictt[i] += 1
            else:
                dictt[i] = 1
        for key,value in dictt.items():
            if value > len(nums) / 2:
                return key