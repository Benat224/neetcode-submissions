'''class Solution:
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
'''

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(heights) - 1
        maxi = 0
        while ptr1 < ptr2:
            aux = min(heights[ptr1], heights[ptr2]) * (ptr2 - ptr1)
            maxi = max(maxi, aux)
            if heights[ptr2] > heights[ptr1]:
                ptr1 += 1
            else:
                ptr2 -= 1
            
        return maxi




















