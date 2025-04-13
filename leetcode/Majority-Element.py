class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        res = maxCount = 0

        for n in nums:
            hashmap[n] += 1
            if maxCount < hashmap[n]:
                maxCount = hashmap[n]
                res = n
        return res