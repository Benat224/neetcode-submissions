class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counter_left, counter_right = 1, 1
        register, result = [], []
        for i, val in enumerate(nums):
            register.append([counter_left, counter_right])
            counter_left *= val
        for i, val in enumerate(nums[::-1]):
            register[len(nums)-i-1][1] = counter_right
            counter_right *= val
        for i, val in enumerate(register):
            result.append(val[0]*val[1])

        print(register)

        return result