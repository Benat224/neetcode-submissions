class Solution:
    def isPalindrome(self, s: str) -> bool:
        aux_s = ''
        for char in s:
            if (char >= 'a' and char <='z') or (char >= 'A' and char <= 'Z') or ( char >= '0' and char <= '9'):
                aux_s+= char.lower()
        return aux_s == aux_s[::-1]