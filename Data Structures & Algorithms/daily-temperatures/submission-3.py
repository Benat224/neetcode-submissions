class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i, val in enumerate(temperatures[::-1]):    
            while stack and stack[-1][1] <= val:
                stack.pop()
            if stack:
                res[len(temperatures)-i-1] = stack[-1][0]-(len(temperatures)-i-1)
            stack.append([len(temperatures)-i-1,val])
        return res