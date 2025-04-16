class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = defaultdict(int)
        for n in nums:
            countmap[n] += 1
    
        bucket = [[] for _ in range(len(nums)+1)]
        for key, value in countmap.items():
            bucket[value].append(key)
        res = []
        for i in range(len(nums), 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
