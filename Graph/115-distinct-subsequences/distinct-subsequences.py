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

    def spaceOptHelper(self, string1, string2):
        ## Length of strings 
        l1 = len(string1)
        l2 = len(string2)

        ## Initialise base case array: ahead
        ahead = [1]*(l2+1)

        ## Iterate over the strings
        for index1 in range(l1-1, -1, -1):
            curr = [0]*(l2+1)
            for index2 in range(l2-1, -1, -1):
                ## Calculate all possible cases
                # Letters Match
                if string1[index1] == string2[index2]:
                    take = ahead[index2+1]
                    notTake = curr[index2+1]

                    # Update curr
                    curr[index2] = take + notTake

                # Letters don't match
                else:
                    notTake = curr[index2+1]
                    curr[index2] = notTake

            ahead = curr.copy()

        return ahead[0]

    def numDistinct(self, string2: str, string1: str) -> int:
        ## Length of strings 
        l1 = len(string1)
        l2 = len(string2)

        ## Initialise dp array
        dp = [[-1]*(l2+1) for _ in range(l1+1)]

        ## Call memoHelper and return 
        # return self.memoHelper(0, 0, string1, string2, dp)

        ##### SPACE OPTIMIZATIONS #####
        return self.spaceOptHelper(string1, string2)