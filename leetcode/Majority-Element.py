class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        res = 0
        most = 0
        for n in nums:
            freq[n] += 1
            if freq[n] > most:
                res = n
                most = freq[n]
        return res