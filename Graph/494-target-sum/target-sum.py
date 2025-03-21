class Solution:
    def memoHelper(self, index, target, nums, dp, n):
        ## Base Cases
        if index == n:
            if target == 0:
                return 1
            else:
                return 0

        ## Return memoized result if present
        if dp[index][target] != -1:
            return dp[index][target]

        ## Calculate possible cases
        take = self.memoHelper(index+1, target-nums[index], nums, dp, n) if target >= nums[index] else 0
        notTake = self.memoHelper(index+1, target, nums, dp, n)

        ## Memoize and return all possible cases
        dp[index][target] = take + notTake
        return dp[index][target]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ## Logic
        # total = sum of all elements of array
        # We essentially need S1 - S2 = target
        # S1 + S2 = total
        # S1 = (total + target)//2

        ####### MEMOIZATION ######
        ## Array size
        n = len(nums)

        ## Sum of all elements
        total = sum(nums)

        ## New target
        if (target + total) % 2 != 0 or total < abs(target):
            return 0
        else:
            newTarget = (target+total)//2

        ## Initialize dp array
        dp = [[-1]*(newTarget+1) for _ in range(n)]

        ## Call function and return answer
        return self.memoHelper(0, newTarget, nums, dp, n)