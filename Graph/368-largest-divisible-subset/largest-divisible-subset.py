class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ## Length of array
        n = len(nums)

        ## Initialize dp array
        dp = [1]*(n)

        ## Initialize required variables
        maxLen = 1
        maxIndex = 0

        ## Initialize hashArray
        hashArr = [i for i in range(n)]

        ## Sort the nums
        nums = sorted(nums)

        ## Iterate over the array
        for index in range(n):
            for prevIndex in range(index):
                if not nums[index] % nums[prevIndex] or not nums[prevIndex] % nums[index]:
                    if dp[index] <= dp[prevIndex] + 1:
                        dp[index] = dp[prevIndex] + 1
                        hashArr[index] = prevIndex

                if maxLen < dp[index]:
                    maxLen = dp[index]
                    maxIndex = index

        ## Make the subset
        answer = []
        while maxIndex != hashArr[maxIndex]:
            answer.append(nums[maxIndex])
            maxIndex = hashArr[maxIndex]

        answer.append(nums[maxIndex])

        return list(reversed(answer))        

            

        