# Problem Link:https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = str()
        for i in s:
            if i.isalpha() or i.isdigit():
                newStr += i
        newStr = newStr.lower()
        x = 0
        y = len(newStr) - 1
        for i in range(len(newStr) // 2):
            if newStr[x] != newStr[y]:
                return False
            x += 1
            y -= 1
        return True