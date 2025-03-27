class Solution:
    def memoHelper(self, index1, index2, string1, string2, dp):
        ## Length of strings
        l1 = len(string1)
        l2 = len(string2)

        ## Base case
        if index1 == l1 and index2 == l2:
            return 1

        if index1 == l1:
            while index2 < l2:
                if string2[index2] != '*':
                    return 0
                index2 += 1
            return 1

        if index2 == l2:
            return 0

        ## Return memoized result if present
        if dp[index1][index2] != -1:
            return dp[index1][index2]

        ## Calculate all possible cases
        # Letters match or '?'
        if string1[index1] == string2[index2] or string2[index2] == '?':
            dp[index1][index2] = self.memoHelper(index1+1, index2+1, string1, string2, dp)
            return dp[index1][index2]

        # Letters is '*'
        elif string2[index2] == '*':
            notTake = self.memoHelper(index1, index2+1, string1, string2, dp)
            take = self.memoHelper(index1+1, index2, string1, string2, dp)

            dp[index1][index2] = max(take, notTake)
            return dp[index1][index2]

        # Letters can't match
        else:
            dp[index1][index2] = 0
            return 0

    def isMatch(self, string1: str, string2: str) -> bool:
        ## Length of strings
        l1 = len(string1)
        l2 = len(string2)

        ## Initalize dp array
        dp = [[-1]*(l2+1) for _ in range(l1+1)]

        ## Call memeHelper and return
        return bool(self.memoHelper(0, 0, string1, string2, dp))   