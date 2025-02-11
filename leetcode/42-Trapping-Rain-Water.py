class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        if length == 0:
            return 0
            
        result = 0

        leftPeak = [0] * length
        rightPeak = [0] * length

        leftPeak[0] = height[0]
        for i in range(1, length):
            leftPeak[i] = max(leftPeak[i-1], height[i])

        rightPeak[length-1] = height[length-1]
        for i in range(length-2, -1, -1):
            rightPeak[i] = max(rightPeak[i+1], height[i])

        for i in range(length):
            currentTrappedWater = min(leftPeak[i], rightPeak[i]) - height[i]
            result += currentTrappedWater

        return result
