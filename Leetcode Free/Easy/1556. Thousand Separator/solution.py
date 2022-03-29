class Solution:
    def thousandSeparator(self, n: int) -> str:
        ans = ''
        while n > 0:
            if len(ans) % 4 == 3:
                ans = '.' + ans
            ans = str(n % 10) + ans
            n //= 10
        if ans:
            return ans
        return '0'
        