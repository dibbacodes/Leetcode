class Solution:
    def minInsertions(self, s: str) -> int:
        ## Strings
        string1 = s
        string2 = s[::-1]

        ## Size of strings
        n = len(string1)

        ## Initialize dp table
        dp = [[0]*(n+1) for _ in range(n+1)]

        ## Base Case
        # dp[n][index2] = 0

        ## lenLCS
        lenLCS = 0

        ## Iterate over the strings and fill dp table
        for index1 in range(n-1, -1, -1):
            for index2 in range(n-1, -1, -1):
                ## Letters match
                if string1[index1] == string2[index2]:
                    dp[index1][index2] = 1 + dp[index1+1][index2+1]

                ## Letters don't match
                else:
                    dp[index1][index2] = max(dp[index1+1][index2],dp[index1][index2+1])

                lenLCS = max(lenLCS, dp[index1][index2])

        return n - lenLCS
