class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        color = 0
        i = 0
        while color < 3:
            for c in range(freq[color]):
                nums[i] = color
                i += 1
            color += 1
        