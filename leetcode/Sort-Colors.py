class Solution:
    def sortColors(self, nums: List[int]) -> None:
        \\\
        Do not return anything, modify nums in-place instead.
        \\\
        occurences = [0] * 3

        for n in nums:
            occurences[n] += 1

        n = 0
        for i in range(3):
            for j in range(occurences[i]):
                nums[n] = i
                n += 1
        