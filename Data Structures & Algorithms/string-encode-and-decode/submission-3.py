class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""
        for word in strs:
            sol += str(len(word)) + "#" + word
        return sol

    def decode(self, s: str) -> List[str]:
        sol = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            sol.append(s[i:j])
            i = j
            
        return sol
        

