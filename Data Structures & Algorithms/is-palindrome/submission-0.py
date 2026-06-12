class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for char in s:
            if char.isalnum():
                string += char.lower()
        first = 0
        last = len(string) - 1
        while first < last:
            if string[first] != string[last]:
                return False
            first += 1
            last -= 1
        return True