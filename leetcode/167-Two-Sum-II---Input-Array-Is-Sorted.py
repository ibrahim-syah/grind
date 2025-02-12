class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n == 0:
            return None
        
        l, r = 0, n-1

        while l <= r:
            twoSum = numbers[l] + numbers[r]
            if twoSum > target:
                r -= 1
            elif twoSum < target:
                l += 1
            else:
                return [l+1, r+1]
        return None