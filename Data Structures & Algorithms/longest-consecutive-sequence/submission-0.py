class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = set()
        for num in nums:
            dic.add(num)
        maxi = 0
        for num in dic:
            count = 0
            if num - 1 not in dic:
                aux = num
                while aux in dic:
                    count += 1
                    aux += 1
                if count > maxi:
                    maxi = count
        return maxi