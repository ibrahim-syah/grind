class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countmap = {}
        for col in range(3):
            countmap[col] = 0
        for n in nums:
            countmap[n] = countmap.get(n, 0) + 1

        color = 0
        i = 0
        # for i in range(len(nums)):
        while color < 3:
            for c in range(countmap[color]):
                nums[i] = color
                i += 1
            color += 1