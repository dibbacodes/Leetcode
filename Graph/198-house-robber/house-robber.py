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
        ##### MEMOIZATION: Top Down #####

        # Define size of nums
        n = len(nums)

        # Initialize dp array
        # dp = [-1]*n

        # Call helpRob function and return the answer
        # return self.helpRob(0, nums, dp, n)

        ####### TABULATION: Bottom-Up #######

        ## Inititalize dp array
        dp = [0]*(n+1)

        ## Base Cases

        # Return 0 if we start robbing after the last house
        dp[n] = 0

        # Iterate through all the houses
        for index in range(n-1, -1, -1):

            # Rob the current house
            robHouse = nums[index]
            if index+2 < n:
                robHouse += dp[index+2]

            # Skip the current house
            skipHouse = 0
            if index+1 < n:
                skipHouse += dp[index+1]

            dp[index] = max(robHouse, skipHouse)

        return dp[0]
            