class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        res = 0
        while i < j:
            val_i, val_j = heights[i], heights[j]
            res = max(res, min(val_i, val_j)*(j-i))
            if val_i >= val_j:
                j -= 1
            else:
                i += 1
        return res