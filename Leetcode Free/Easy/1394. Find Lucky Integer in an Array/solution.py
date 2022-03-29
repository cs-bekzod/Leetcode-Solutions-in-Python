class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dictt = dict()
        mylist = list()
        for i in arr:
            if i in dictt.keys():
                dictt[i] += 1
            else:
                dictt[i] = 1
        
        for key,value in dictt.items():
            if key == value:
                mylist.append(key)
        try:      
            return max(mylist)
        except:
            return -1
                