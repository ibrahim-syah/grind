class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        nums.sort()

        currentSequenceNumber = nums[0]
        currentSequenceStreak = 0
        numsIndex = 0

        while numsIndex < len(nums):
            if nums[numsIndex] != currentSequenceNumber:
                currentSequenceNumber = nums[numsIndex] # start a new sequence
                currentSequenceStreak = 0
            while numsIndex < len(nums) and currentSequenceNumber == nums[numsIndex]:
                numsIndex += 1
            currentSequenceNumber += 1
            currentSequenceStreak += 1
            res = max(res, currentSequenceStreak)

        return res