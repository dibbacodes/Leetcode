class Solution:
    def helper(self, index: int, nums: List[int], 
    dp: List[int], n: int) -> int:
        # base case
        if(index >= n):
            return 0

        # memoization
        if(dp[index] != -1):
            return dp[index]

        # recursion
        rob = nums[index] + self.helper(index+2, nums, dp, n)
        not_rob = 0 + self.helper(index+1, nums, dp, n)

        dp[index] = max(rob, not_rob)
        return dp[index]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n

        return self.helper(0, nums, dp, n)