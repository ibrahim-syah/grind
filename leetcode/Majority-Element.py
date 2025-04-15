class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = nums[0]
        maxCount = 0

        for n in nums:
            count[n] += 1
            if count[n] > maxCount:
                res = n
                maxCount = count[n]
        return res