class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        array = [0] * 26
        arrayAux = [0] * 26
        for letter in s1:
            array[ord(letter) - ord("a")] += 1
        f = 0
        for l in range(len(s2)):         
            arrayAux[ord(s2[l]) - ord("a")] += 1
            if l >= len(s1):
                arrayAux[ord(s2[f]) - ord("a")] -= 1
                f += 1
            if arrayAux == array:
                return True
        return False
             