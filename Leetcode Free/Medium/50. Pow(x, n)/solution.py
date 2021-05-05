class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n > 0:
                return x ** n
        if n < 0:
            return x ** n

        return 1