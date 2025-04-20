class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        occurences = defaultdict(int)
        maxCount, res = -1, nums[0]

        for n in nums:
            occurences[n] += 1
            if maxCount < occurences[n]:
                maxCount = occurences[n]
                res = n
        return res
        
