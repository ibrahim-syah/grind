class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums)+1)]

        hashmap = defaultdict(int)
        for n in nums:
            hashmap[n] += 1

        for key, value in hashmap.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(nums), -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) >= k:
                    return res
        return res