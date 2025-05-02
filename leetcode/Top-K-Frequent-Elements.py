class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        bucket = [[] for _ in range(len(nums)+1)]
        for key, val in freq.items():
            bucket[val].append(key)
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for count in bucket[i]:
                res.append(count)
                if len(res) >= k:
                    return res
        return res