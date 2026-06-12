class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) -1
        while i < j:
            val = numbers[i] + numbers [j]
            if val == target:
                return [i+1, j+1]
            if val < target:
                i += 1
            if val > target:
                j -= 1
        