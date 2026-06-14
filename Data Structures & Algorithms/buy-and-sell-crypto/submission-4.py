class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mini = prices[0]
        for i in range(1,len(prices)):
            val = prices[i]
            res = max(res, (val-mini))
            if val < mini:
                mini = val
        return res