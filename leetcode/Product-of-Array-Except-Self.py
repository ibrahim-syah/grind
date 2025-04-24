class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = [0] * len(nums)
        for i in range(len(prefix)):
            prefix[i] = product
            product *= nums[i]
        suffix = [0] * len(nums)
        product = 1
        for i in range(len(suffix)-1, -1, -1):
            suffix[i] = product
            product *= nums[i]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res