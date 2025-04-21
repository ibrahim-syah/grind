class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        i = 0
        color = 0
        while i < len(nums):
            for c in range(freq[color]):
                nums[i] = color
                i += 1
            color += 1
        