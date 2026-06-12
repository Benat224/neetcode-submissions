'''class Solution:
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
        return temperatures'''


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        'saves the biggest value at the end and smaller values but more recent before'
        stack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)-1,-1, -1):
            while len(stack) != 0 and stack[-1][0] <= temperatures[i]:
                stack.pop()
            if len(stack) != 0:
                result[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return result



















