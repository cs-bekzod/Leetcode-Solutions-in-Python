class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ''
        for i in address:
            if i != '.':
                result += i
            else:
                result += '[.]'
        return result