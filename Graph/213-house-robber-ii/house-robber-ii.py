class Solution:
    def helpRob(self, index, nums, dp, n) -> int:
        ## Base Cases
        
        # Return 0: if index is beyond number of houses
        if index >= n:
            return 0

        ## Return cached result if available
        if dp[index] != -1:
            return dp[index]

        ## Calculate all possible options
        robHouse = nums[index] + self.helpRob(index+2, nums, dp, n)
        skipHouse = 0 + self.helpRob(index+1, nums, dp, n)

        ## Memoize and return max value
        dp[index] = max(robHouse, skipHouse)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [-1]*n
        dp2 = [-1]*n

        if n==1:
            return nums[0]
        
        skipHouse1 = self.helpRob(1, nums, dp1, n)
        skipHouse2 = self.helpRob(0, nums, dp2, n-1)

        return max(skipHouse1, skipHouse2)