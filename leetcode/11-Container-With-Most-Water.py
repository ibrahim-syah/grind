class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return None
        water = 0

        l, r = 0, n-1
        while l < r:
            water = max(water, (r-l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return water