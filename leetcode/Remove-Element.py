class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
                length += 1
        return length
                