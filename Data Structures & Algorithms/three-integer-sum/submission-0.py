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
                target = nums[i]
                num = nums[f] + nums[l]
                if num + target < 0:
                    f += 1
                if num + target > 0:
                    l -= 1
                if num + target == 0:
                    result.append([nums[i], nums[f] , nums[l]])
                    f += 1
                    l -= 1
                    while f < l and nums[f] == nums[f - 1]:
                        f += 1
        return result