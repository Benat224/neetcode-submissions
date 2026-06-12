class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set(nums)
        maxi = 0
        for num in dic:
            if num - 1 not in dic:
                length = 1
                while num + length in dic:
                    length += 1
                maxi = max(length, maxi)
        return maxi