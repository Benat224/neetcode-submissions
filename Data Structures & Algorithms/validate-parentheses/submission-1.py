class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter in ["]", ")", "}"]:
                if len(stack) == 0:
                    return False
                elem = stack.pop()
                if letter == "]" and elem != "[" or letter == ")" and elem != "(" or letter == "}" and elem != "{":
                    return False 
            else:
                stack.append(letter)
        if len(stack) == 0:
            return True
        return False