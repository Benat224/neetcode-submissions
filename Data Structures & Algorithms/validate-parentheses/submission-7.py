class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for val in s:
            if val in ['(', '{', '[']:
                stack.append(val)
            else:
                if len(stack) == 0:
                    return False
                aux = stack.pop()
                if aux not in  ['(', '{', '['] or  aux == '(' and val != ')' or aux == '[' and val != ']' or aux == '{' and val != '}':
                    return False
        return len(stack) == 0
                    