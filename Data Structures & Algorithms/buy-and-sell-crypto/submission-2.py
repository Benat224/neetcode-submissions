class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0
        for n in prices:
            if n < lowest:
                lowest = n
            res = max(res, n - lowest)
        return res