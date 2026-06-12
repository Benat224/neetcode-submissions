'''class Solution:
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

'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        ptr1 = 0
        ptr2 = len(numbers) - 1

        while(numbers[ptr1] + numbers[ptr2] != target):
            if numbers[ptr1] + numbers[ptr2] > target :
                ptr2 -=1
            else:
                ptr1 += 1

        return [ptr1 + 1, ptr2 + 1]
















