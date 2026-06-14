class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def apply(p1, p2, s:str):
            if s == '+':
                return int(p1) + int(p2)
            if s == '-':
                return int(p1) - int(p2)
            if s == '*':
                return  int(p1) * int(p2)
            if s == '/':
                return int(p1) / int(p2)

        stack = []
        for val in tokens:
            if val in ['+', '-', '*', '/']:
                aux = apply(stack[-2], stack[-1], val)
                stack.pop()
                stack.pop()
                stack.append(aux)
            else:
                stack.append(val)
        return int(stack[-1])
