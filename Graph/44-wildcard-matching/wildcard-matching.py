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

    def tabulationHelper(self, string1, string2):
        ## Length of strings
        l1 = len(string1)
        l2 = len(string2)

        ## Initalize dp array
        dp = [[0]*(l2+1) for _ in range(l1+1)] 

        ## Base cases  
        dp[l1][l2] = 1

        for index2 in range(l2-1, -1, -1):
            if string2[index2] != '*':
                break
            else:
                dp[l1][index2] = 1
        
        ## Iterate over the strings
        for index1 in range(l1-1, -1, -1):
            for index2 in range(l2-1, -1, -1):
                ## Calculate all possible cases
                # Letters match or '?'
                if string1[index1] == string2[index2] or string2[index2] == '?':
                    dp[index1][index2] = ahead[index2+1]

                # Letters is '*'
                elif string2[index2] == '*':
                    notTake = dp[index1][index2+1]
                    take = ahead[index2]

                    dp[index1][index2] = max(take, notTake)

                # Letters can't match
                else:
                    dp[index1][index2] = 0

        return dp[0][0]

    def spaceOptHelper(self, string1, string2):
        ## Length of strings
        l1 = len(string1)
        l2 = len(string2)

        ## Initalize base case array
        ahead = [0]*(l2+1)

        ## Base cases  
        ahead[l2] = 1

        for index2 in range(l2-1, -1, -1):
            if string2[index2] != '*':
                break
            else:
                ahead[index2] = 1
        
        ## Iterate over the strings
        for index1 in range(l1-1, -1, -1):
            curr = [0]*(l2+1)
            for index2 in range(l2-1, -1, -1):
                ## Calculate all possible cases
                # Letters match or '?'
                if string1[index1] == string2[index2] or string2[index2] == '?':
                    curr[index2] = ahead[index2+1]

                # Letters is '*'
                elif string2[index2] == '*':
                    notTake = curr[index2+1]
                    take = ahead[index2]

                    curr[index2] = max(take, notTake)

                # Letters can't match
                else:
                    curr[index2] = 0
            
            ahead = curr.copy()

        return ahead[0]

    def isMatch(self, string1: str, string2: str) -> bool:
        ## Length of strings
        # l1 = len(string1)
        # l2 = len(string2)

        # ## Initalize dp array
        # dp = [[-1]*(l2+1) for _ in range(l1+1)]

        # ## Call memoHelper and return
        # # return bool(self.memoHelper(0, 0, string1, string2, dp))  

        # ###### TABULATION #######
        # return bool(self.tabulationHelper(string1, string2))

        ##### SPACE OPTIMIZATION #######
        return bool(self.spaceOptHelper(string1, string2))