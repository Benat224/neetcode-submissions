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
            
        #return result

        total = 1
        i = -1
        res = [0]*len(nums)
        for j, val in enumerate(nums):
            total *= val
            if val == 0:
                i = j
                break
        if i != -1:
            total = 1
            for i, val in enumerate(nums):
                if i != j:
                    total *= val
            res[j] = total
            return res
        for i, val in enumerate(nums): 
            res[i] = int(total/val)
    
        return res
        return result