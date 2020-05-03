class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rr = list(magazine)
        count=0
        for i in ransomNote:
            if(i in rr):
                rr.remove(i)
                count += 1
        if(len(ransomNote)==count):
            return True
        else:
            return False
                
