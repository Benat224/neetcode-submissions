class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        i = 0
        while i < len(tokens):
            while tokens[i] not in ['+', '-', '*', '/']:
                stack.append(int(tokens[i]))
                i += 1
            aux = tokens[i]
            aux2 = stack.pop()
            aux1 = stack.pop()
            if aux == "+":
                aux = aux1 + aux2
            elif aux == "-":
                aux = aux1 - aux2
            elif aux == "*":
                aux = aux1 * aux2
            elif aux == "/":
                aux = int(float(aux1) / aux2)
            stack.append(aux)
            i += 1
            
        return stack[0]