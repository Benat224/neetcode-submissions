class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        res = 0
        while i < j:
            val_i, val_j = heights[i], heights[j]
            res = max(res, min(val_i, val_j)*(j-i))
            val_i_1, val_j_1 = heights[i+1], heights[j-1]
            if val_i >= val_j:
                j -= 1
            else:
                i += 1
            # if val_i_1 <= val_i and val_j_1 <= val_j:
            #     i +=1
            #     j-=1
            # elif val_i_1 <= val_i:
            #     j -=1
            # elif val_j_1 <= val_j:
            #     i +=1
            # else:
            #     if val_i_1 >= val_i_1:
            #         j -= 1
            #     else:
            #         i += 1
        return res