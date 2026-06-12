class Solution:
        def generateParenthesis(self, n: int) -> List[str]:
            sol = []
            s = []
            numO, numC = 0, 0
            def backtrack(numO, numC):
                if numO == numC == n:
                    sol.append("".join(s))
                    return
                if numO < n:
                    s.append('(')
                    backtrack(numO + 1, numC)
                    s.pop()
                if numC < numO:
                    s.append(')')
                    backtrack(numO, numC + 1)
                    s.pop()      
            
            backtrack(0, 0)
            return sol