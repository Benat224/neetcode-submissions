class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculate(k:int) -> int:
            counter = 0
            for val in piles:
                counter += -(-val//k)
            return counter
        
        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l)//2
            if calculate(m) > h:
                l = m + 1
            else:
                r = m
        
        return l