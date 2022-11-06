class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = currsum = nums[0]
        
        for i in range(1,len(nums)):
            if currsum < 0:
                currsum = 0
            currsum += nums[i]
            if currsum > maxsum:
                maxsum = currsum
        return maxsum