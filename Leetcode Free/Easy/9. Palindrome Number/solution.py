# Problem link: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            return x == int(str(x)[::-1])

        return False
        