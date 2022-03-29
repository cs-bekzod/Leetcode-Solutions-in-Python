# Problem Link:https://leetcode.com/problems/power-of-two
import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        try:
            if 2 ** int(math.log(n,2)) == n:
                return True
        except:
            return False

print(Solution().isPowerOfTwo(1))
