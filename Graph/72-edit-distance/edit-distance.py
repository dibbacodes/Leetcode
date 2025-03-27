class Solution:
    INF = 1e9
    def memoHelper(self, index1, index2, word1, word2, dp):
        ## Length of words
        l1 = len(word1)
        l2 = len(word2)

        ## Base case
        if index2 == l2:
            return l1 - index1
        if index1 == l1:
            return l2 - index2

        ## Return memoized result if available
        if dp[index1][index2] != -1:
            return dp[index1][index2]

        ## Calculate all cases
        # Letters match
        if word1[index1] == word2[index2]:
            dp[index1][index2] = self.memoHelper(index1+1, index2+1, word1, word2, dp)
            return dp[index1][index2]

        # Letters don't match
        else:
            replace = 1 + self.memoHelper(index1+1, index2+1, word1, word2, dp)
            insert = 1 + self.memoHelper(index1, index2+1, word1, word2, dp)
            delete = 1 + self.memoHelper(index1+1, index2, word1, word2, dp)

            dp[index1][index2] = min(replace, insert, delete)
            return dp[index1][index2]

    def minDistance(self, word1: str, word2: str) -> int:
        ## Length of words
        l1 = len(word1)
        l2 = len(word2)

        ## Initialize dp array
        dp = [[-1]*(l2+1) for _ in range(l1+1)]

        ## Call memoHelper and return answer
        return self.memoHelper(0, 0, word1, word2, dp)