class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter, result = 0, 0
        discard_set = set(nums)
        while len(discard_set) != 0:
            num = discard_set.pop()
            counter = 1
            lower, greater = num, num
            while lower-1 in discard_set:
                lower -= 1
                counter += 1
                discard_set.remove(lower)
            while greater+1 in discard_set:
                greater += 1
                counter += 1 
                discard_set.remove(greater)
            if counter > result:
                result = counter

        return result