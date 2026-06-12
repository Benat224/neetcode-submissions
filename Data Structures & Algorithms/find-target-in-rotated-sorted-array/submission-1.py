'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f, l = 0, len(nums) - 1
        while f <= l:
            m = (l - f) // 2
            val = nums[m]
            if val == target:
                return m
            aux1, aux2 = nums[f], nums[l]
            
            if aux1 <= target:
                if target <= val:
                    l = m - 1
                else:
                    f = m + 1
            else:
                if target <= val:
                    l = m - 1
                else:
                    f = m + 1


        return -1
'''



class Solution:
    def searchHelp(self, nums: List[int], target: int, f: int, l: int) -> int:
        if (l - f) <= 1:
            if nums[f] == target:
                return f
            elif nums[l] == target:
                return l
            else:
                return -1

        m = (f + l) // 2
        p1 = nums[f]
        p2 = nums[m]
        p3 = nums[l]

        if target == p2:
            return m
        
        if p1 < p3:    
            if target < p2:
                return self.searchHelp(nums, target, f, m-1)
            else:
                return self.searchHelp(nums, target, m+1, l)
        else:
            if p1 < p2:
                if p1 <= target < p2:
                    return self.searchHelp(nums, target, f, m-1)
                else:
                    return self.searchHelp(nums, target, m+1, l)
            else:
                if p2 < target <= p3:
                    return self.searchHelp(nums, target, m+1, l)
                else:
                    return self.searchHelp(nums, target, f, m-1)

    def search(self, nums: List[int], target: int) -> int:
        f = 0
        l = len(nums) - 1
        return self.searchHelp(nums, target, f, l)  # Llamar a searchHelp con self







