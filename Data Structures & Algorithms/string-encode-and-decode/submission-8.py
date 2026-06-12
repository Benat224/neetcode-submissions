class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for elem in strs:
            s += str(len(elem)) + ','
        s += '#'
        for elem in strs:
            s += elem
        return s
    def decode(self, s: str) -> List[str]:
        result = []
        l = []
        pos_counter = 0
        s_count = 0
       
        while s[s_count] != '#':
            aux = ""
            while s[s_count] != ',':
                aux += s[s_count]
                s_count += 1
            l.append(int(aux))
            s_count += 1
        s_count += 1
        for i in range(len(l)):
            result.append(s[s_count:s_count + l[i]])
            s_count += l[i]

        return result


