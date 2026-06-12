class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            f, l = 1, max(piles)
            sol = l
            while f <= l:
                m = (f + l) // 2
                cont = 0
                for i in piles:
                    cont += (i + m - 1) // m
                    i += 1
                if cont > h:
                    f = m + 1
                else:
                    sol = m
                    l = m - 1
            return sol