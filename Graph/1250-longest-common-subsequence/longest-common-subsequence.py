class Solution:
    def memoHelper(self, index1, index2, l1, l2, dp, text1, text2):
        ## Base cases
        if index1 == l1 or index2 == l2:
            return 0
        
        ## Return memozied result if possible
        if dp[index1][index2] != -1:
            return dp[index1][index2]

        ## Calculate all possible cases
        # Letters match
        if text1[index1] == text2[index2]:
            dp[index1][index2] = 1 + self.memoHelper(index1+1, index2+1, l1, l2, dp, text1, text2)
            return dp[index1][index2]

        # Letters don't match
        else:
            moveIndex1 = self.memoHelper(index1+1, index2, l1, l2, dp, text1, text2)
            moveIndex2 = self.memoHelper(index1, index2+1, l1, l2, dp, text1, text2)

            dp[index1][index2] = max(moveIndex1, moveIndex2)
            return dp[index1][index2]

    def tabulationHelper(self, text1, text2):
        ## Size of strings
        l1 = len(text1)
        l2 = len(text2)

        ## Initialize dp array
        dp = [[0]*(l2+1) for _ in range(l1+1)]

        ## Base cases
        # dp[index1][l2] = 0
        # dp[l1][index2] = 0

        ## Iterate over the strings
        for index1 in range(l1-1, -1, -1):
            for index2 in range(l2-1, -1, -1):
                # Letters match
                if text1[index1] == text2[index2]:
                    dp[index1][index2] = 1 + dp[index1+1][index2+1]

                # Letters don't match
                else:
                    moveIndex1 = dp[index1+1][index2]
                    moveIndex2 = dp[index1][index2+1]

                    dp[index1][index2] = max(moveIndex1, moveIndex2)

        return dp[0][0]
 
    def spaceOptHelper(self, text1, text2):
        ## Size of strings
        l1 = len(text1)
        l2 = len(text2)

        ## Initialize base case array: ahead
        ahead = [0]*(l2+1) 

        ## Base cases
        # ahead[l2] = 0

        ## Iterate over the strings
        for index1 in range(l1-1, -1, -1):
            curr = [0]*(l2+1)
            for index2 in range(l2-1, -1, -1):
                # Letters match
                if text1[index1] == text2[index2]:
                    curr[index2] = 1 + ahead[index2+1]

                # Letters don't match
                else:
                    moveIndex1 = ahead[index2]
                    moveIndex2 = curr[index2+1]

                    curr[index2] = max(moveIndex1, moveIndex2)

            ahead = curr.copy()

        return ahead[0]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # #### MEMOIZATION ####
        # ## Size of strings
        # l1 = len(text1)
        # l2 = len(text2)

        # ## Initialize dp array
        # dp = [[-1]*l2 for _ in range(l1)]

        # ## Call memoHelper and return answer
        # return self.memoHelper(0, 0, l1, l2, dp, text1, text2)

        ##### TABULATION #####
        # return self.tabulationHelper(text1, text2)

        ##### SPACE OPTIMIZATION #####
        return self.spaceOptHelper(text1, text2)
