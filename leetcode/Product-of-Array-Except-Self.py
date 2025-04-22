class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        prefix = [0] * len(nums)
        for i in range(len(nums)):
            prefix[i] = product
            product *= nums[i]

        product = 1
        suffix = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = product
            product *= nums[i]

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]

        return res
            
