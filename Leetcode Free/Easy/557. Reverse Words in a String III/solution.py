class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        MyList = s.split(" ")
        for i in MyList[:len(MyList)-1]:
                result += i[::-1] + " "
        return result + MyList[-1][::-1]