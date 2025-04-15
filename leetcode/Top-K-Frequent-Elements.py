class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {}
        bucket = [[] for i in range(len(nums) + 1)]

        for n in nums:
            countmap[n] = countmap.get(n, 0) + 1
        
        for n, v in countmap.items():
            bucket[v].append(n)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res