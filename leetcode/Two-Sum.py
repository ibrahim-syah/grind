class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complementmap:
                return [i, complementmap[complement]]
            else:
                complementmap[nums[i]] = i
        