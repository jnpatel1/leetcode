class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        runningsum = nums[0]
        end = 1
        
        while end < len(nums):
            if runningsum + nums[end] < nums[end]:
                runningsum = nums[end]
            
            else:
                runningsum += nums[end]

            if runningsum > maxsum:
                maxsum = runningsum
            
            end += 1
        

        return maxsum