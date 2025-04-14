class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        hashmap = defaultdict(int)
        res = maxCount = 0
        for n in nums:
            hashmap[n] += 1
            if hashmap[n] > length / 2:
                return n
            # if hashmap[n] > maxCount:
            #     maxCount = hashmap[n]
            #     res = n
        return res
        