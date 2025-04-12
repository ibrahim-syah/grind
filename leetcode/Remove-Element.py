class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        originalLen = len(nums)
        k = 0
        for i in range(originalLen):
            while nums[i] == val:
                nums[i] = \_\
                k += 1
                nums[i], nums[originalLen-k] = nums[originalLen-k], nums[i]

        return originalLen-k

            