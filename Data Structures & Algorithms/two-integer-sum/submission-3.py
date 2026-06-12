class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        col = {}
        for i in range(len(nums)):
            if nums[i] not in col:
                col[nums[i]] = [i]
            else:
                col[nums[i]].append(i)

        for n in col:
            aux = col.get(target - n, -1)
            if aux != -1:
                if(target == n * 2):
                    if(len(col[n])) >=2:
                        return [aux[0], aux[1]]
                else:
                    return [col[n][0], aux[0]]
