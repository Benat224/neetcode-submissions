class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, n in enumerate(nums):
            if n > 0 or i >= (len(nums) - 2):
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            f = i + 1
            l = len(nums) - 1
            while f < l:
                num = n + nums[f] + nums[l]
                if num < 0:
                    f += 1
                elif num > 0:
                    l -= 1
                else:
                    result.append([n, nums[f], nums[l]])
                    f += 1
                    l -= 1
                    while f < l and nums[f] == nums[f -1]:
                        f += 1
        return result