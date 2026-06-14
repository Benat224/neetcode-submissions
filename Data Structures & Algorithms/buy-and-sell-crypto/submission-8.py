class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mini = prices[0]
        for val in prices:
            res = max(res, (val-mini))
            mini = min(mini, val)
        return res