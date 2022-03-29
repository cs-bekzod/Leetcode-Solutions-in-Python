class Solution:
    def repeatedNTimes(self, A: list[int]) -> int:
        dictt = {}
        for i in A:
            arr = dictt.keys()
            if i in arr:
                dictt[i] += 1
            else:
                 dictt[i] = 1
        for j in dictt.keys():
            if dictt[j] == len(A) // 2:
                return j
        return dictt