class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        ### Fill dp table to get Longest Commons Subseq

        ## Length of strings
        l1 = len(str1)
        l2 = len(str2)

        ## Initialize dp array
        dp = [[0]*(l2+1) for _ in range(l1+1)]

        ## Base Case
        # dp[l1][index2] = 0

        ## Iterate over the strings
        for index1 in range(l1-1, -1, -1):
            for index2 in range(l2-1, -1, -1):
                ## Letters match
                if str1[index1] == str2[index2]:
                    dp[index1][index2] = 1 + dp[index1+1][index2+1]

                ## Letters don't match
                else:
                    dp[index1][index2] = max(dp[index1+1][index2], dp[index1][index2+1])

        ## Generate the supersequence
        answer = ""

        index1 = 0
        index2 = 0

        while index1 < l1 and index2 < l2:
            ## Letter match
            if str1[index1] == str2[index2]:
                answer += str1[index1]
                index1 += 1
                index2 += 1

            ## Letter don't match
            else:
                if dp[index1+1][index2] >= dp[index1][index2+1]:
                    answer += str1[index1]
                    index1 += 1

                else:
                    answer += str2[index2]
                    index2 += 1

        ## Add remaining characters
        while index1 < l1:
            answer += str1[index1]
            index1 += 1

        while index2 < l2:
            answer += str2[index2]
            index2 += 1

        ## Return the supersequence
        return answer
        