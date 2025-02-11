class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashset = set(nums)

        for num in hashset:
            if (num-1) not in hashset:
                streak = 1
                while (num+streak) in hashset:
                    streak += 1
                res = max(res, streak)
        return res