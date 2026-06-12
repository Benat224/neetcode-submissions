class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "@" + word
        return result
       
    def decode(self, s: str) -> List[str]:
        result = []
        i, j = 0, 0
        while j < len(s):
            while s[j] != "@":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j

        return result
                    

