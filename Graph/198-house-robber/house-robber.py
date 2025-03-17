class Solution:
    def helpRob(self, index: int, nums: List[int], dp: List[int], n: int)->int:
        ## Base Cases

        # If index is greater or equal to n: Not possibe to Rob
        if index >= n:
            return 0

        ## Check if this value has already been calculated
        if dp[index] != -1:
            return dp[index]

        ## Go through all possible options
        robHouse = nums[index] + self.helpRob(index+2, nums, dp, n)
        skipHouse = 0 + self.helpRob(index+1, nums, dp, n)

        ## Memoization and return maximum value 
        dp[index] = max(robHouse, skipHouse)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        # Define size of nums
        n = len(nums)

        # Initialize dp array
        dp = [-1]*n

        # Call helpRob function and return the answer
        return self.helpRob(0, nums, dp, n)