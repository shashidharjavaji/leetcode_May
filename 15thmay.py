class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        curr_max = 0
        final_max = 0
        for i in A:
            curr_max += i
            if curr_max <= 0:
                curr_max = 0
            if final_max < curr_max:
                final_max = curr_max
        if final_max == 0:
            return max(A)
        
        curr_min = 0
        final_min = 0
        for i in A:
            curr_min += i
            if curr_min >= 0:
                curr_min = 0
            if final_min > curr_min:
                final_min = curr_min
        return max(final_max, sum(A) - final_min)
    
