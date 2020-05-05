class Solution:
    def firstUniqChar(self, s: str) -> int:
        fre=Counter(s)
        key=[]
        for i in fre:
            key.append(i)
        for j in key:
            if(fre[j]==1):
                return int(s.index(j))
        return -1
        
