# Problem link: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return 0
        elif x > 0:
            result = int(str(x)[::-1])
        else:
            result = int('-' + str(x * -1)[::-1])
        if result >= 2 ** 31 - 1 or result <= -2 ** 31:
            return 0
        return result

