class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f = 0
        l = len(numbers) - 1
        while True:
            num = numbers[f] + numbers[l]
            if num > target:
                l -= 1
            if num < target:
                f += 1
            if num == target:
                return [f + 1, l + 1]