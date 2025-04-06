class Solution:
    def memoHelper(self, currIndex, prevIndex, nums, dp, n):
        ## Base case
        if currIndex == n:
            return 0

        ## Return memoized result if present
        if dp[currIndex][prevIndex+1] != -1:
            return dp[currIndex][prevIndex+1]

        ## Calculate all cases
        take = 1 + self.memoHelper(currIndex+1, currIndex, nums, dp, n) if prevIndex == -1 or nums[prevIndex] < nums[currIndex] else 0
        notTake = self.memoHelper(currIndex+1, prevIndex, nums, dp, n)

        ## Memoize and return 
        dp[currIndex][prevIndex+1] = max(take, notTake)
        return dp[currIndex][prevIndex+1]

    def tabulationHelper(self, nums):
        ## Lenght of array
        n = len(nums)

        ## Initialize dp array
        dp = [[0]*(n+1) for _ in range(n+1)]

        ## Base Case
        # dp[n][prevIndex] = 0

        ## Iterate over the array
        for currIndex in range(n-1, -1, -1):
            for prevIndex in range(currIndex-1, -2, -1):
                ## Calculate all cases
                take = 1 + dp[currIndex+1][currIndex+1] if prevIndex == -1 or nums[prevIndex] < nums[currIndex] else 0
                notTake = dp[currIndex+1][prevIndex+1]

                dp[currIndex][prevIndex+1] = max(take, notTake)

        return dp[0][0]

    def spaceOptHelper(self, nums):
        ## Length of array
        n = len(nums)

        ## Base case array
        ahead = [0]*(n+1)

        ## Iterate over the array
        for currIndex in range(n-1, -1, -1):
            curr = [0]*(n+1)
            for prevIndex in range(currIndex-1, -2, -1):
                ## Calculate all cases
                take = 1 + ahead[currIndex+1] if prevIndex == -1 or nums[prevIndex] < nums[currIndex] else 0
                notTake = ahead[prevIndex+1]

                curr[prevIndex+1] = max(take, notTake)
            
            ahead = curr.copy()

        return ahead[0]
    
    def spaceOptHelper2(self, nums):
        ## Length of array
        n = len(nums)

        ## Initialize dp array
        dp = [1]*n

        ## Initilize final answer
        maxLen = 1

        ## Iterate over the array and update dp table
        for currIndex in range(n):
            for prevIndex in range(currIndex):
                if nums[currIndex] > nums[prevIndex]:
                    dp[currIndex] = max(dp[currIndex], 1 + dp[prevIndex])
            
            maxLen = max(maxLen, dp[currIndex])

        return maxLen

        

    def lengthOfLIS(self, nums: List[int]) -> int:
        # ## Length of array
        # n = len(nums)

        # ## Initialize dp array
        # dp = [[-1]*(n+1) for _ in range(n+1)]

        # ## Call memoHelper and return answer
        # return self.memoHelper(0, -1, nums, dp, n)

        # return self.tabulationHelper(nums)

        return self.spaceOptHelper2(nums)