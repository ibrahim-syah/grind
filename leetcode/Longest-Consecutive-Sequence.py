class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)

        res = 0
        for n in hashset:
            if n-1 not in hashset:
                count = 1
                while n+count in hashset:
                    count += 1
                res = max(res, count) 
        return res

                

        