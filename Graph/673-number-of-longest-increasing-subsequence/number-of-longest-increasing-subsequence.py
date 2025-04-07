class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        ## Length of list
        n = len(nums)

        ## Initialize required lists
        dp = [1]*(n+1)
        count = [1]*(n+1)

        ## Required variables
        maxLen = 1

        ## Iterate over the array
        for index in range(n):
            for prevIndex in range(index):
                if nums[prevIndex] < nums[index]:
                    # Longer length
                    if 1+dp[prevIndex] > dp[index]:
                        dp[index] = 1+dp[prevIndex]
                        count[index] = count[prevIndex]
                    # Equal length
                    elif 1+dp[prevIndex] == dp[index]:
                        count[index] += count[prevIndex]

            maxLen = max(maxLen, dp[index])

        ## Count the number of LIS
        answer = 0
        for index in range(n):
            if dp[index] == maxLen:
                answer += count[index]

        ## Return answer
        return answer