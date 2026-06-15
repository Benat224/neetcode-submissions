class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        aux = []
        for i in range(len(position)):
            aux.append([position[i], speed[i]])
        aux.sort(key= lambda val: val[0])
        for i in range(len(position)-1,-1, -1):
            pi = aux[i][0]
            si = aux[i][1]
            ti = (target-pi)/si
            if not stack or ti > stack[-1]:
                stack.append(ti)
        return len(stack)