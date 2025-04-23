class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for n in hashset:
            if not n-1 in hashset:
                count = 1
                while n+count in hashset:
                    count += 1
                longest = max(longest, count)
        return longest
        