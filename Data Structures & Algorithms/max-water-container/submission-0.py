class Solution:
    def maxArea(self, heights: List[int]) -> int:
        f = 0
        l = len(heights) - 1
        res = 0
        while f < l:
            a = heights[f]
            b = heights[l]
            res = max(res, (l - f) * min(a, b))        
            if a <= b:
                f += 1
            else:
                l -= 1             
        return res