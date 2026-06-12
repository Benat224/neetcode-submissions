class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [ 0 for _ in range(len(nums))]
        prod = 1
        zeros = []
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                zeros.append(i) 
        
        if len(zeros) >= 2:
            return result

        if len(zeros) == 1:
            result [zeros[0]] = prod
            return result

        for i, n in enumerate(nums):
            result[i] = prod // n
        return result