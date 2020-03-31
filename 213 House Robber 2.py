class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_helper(nums, 0, len(nums) - 2),
                   self.rob_helper(nums, 1, len(nums) - 1))


    def rob_helper(self, nums, low, high):
        prevMax = currMax = 0
        for index in range(low, high + 1):
            temp = currMax
            currMax = max(prevMax + nums[index], currMax)
            prevMax = temp
        return currMax
        
