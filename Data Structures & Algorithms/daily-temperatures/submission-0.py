class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i, n in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < n:
                temperatures[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((n, i))
        while len(stack) != 0:
            aux = stack.pop()
            temperatures[aux[1]] = 0
        return temperatures