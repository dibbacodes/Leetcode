class Solution:
    def memoHelper(self, index1, index2, string1, string2, dp):
        ## Length of strings 
        l1 = len(string1)
        l2 = len(string2)

        ## Base case
        # Target string ends
        if index1 == l1:
            return 1
        # Other string ends before target string
        if index2 == l2:
            return 0

        ## Return memoized result if possible
        if dp[index1][index2] != -1:
            return dp[index1][index2]

        ## Calculate all possible cases
        # Letters Match
        if string1[index1] == string2[index2]:
            take = self.memoHelper(index1+1, index2+1, string1, string2, dp)
            notTake = self.memoHelper(index1, index2+1, string1, string2, dp)

            dp[index1][index2] = take + notTake
            return dp[index1][index2]

        # Letters don't match
        else:
            notTake = self.memoHelper(index1, index2+1, string1, string2, dp)

            dp[index1][index2] = notTake
            return dp[index1][index2]

    def numDistinct(self, string2: str, string1: str) -> int:
        ## Length of strings 
        l1 = len(string1)
        l2 = len(string2)

        ## Initialise dp array
        dp = [[-1]*(l2+1) for _ in range(l1+1)]

        ## Call memoHelper and return 
        return self.memoHelper(0, 0, string1, string2, dp)