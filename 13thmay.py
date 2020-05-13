class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        l = k
        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k = k-1
            stack.append(i)
        answer = "".join(stack[0:len(num)-l]).lstrip("0")
        if(len(answer)):
            return answer
        else:
            return "0"
