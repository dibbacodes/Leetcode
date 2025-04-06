from typing import List

class Solution:

    def isValid(self, word1: str, word2: str) -> bool:
        ## Ensure word1 is the shorter word
        if len(word1) > len(word2):
            word1, word2 = word2, word1

        ## Lengths must differ by exactly 1
        if len(word2) - len(word1) != 1:
            return False

        index1 = index2 = 0
        mismatch_found = False

        ## Check if one character can be inserted to make words equal
        while index1 < len(word1) and index2 < len(word2):
            if word1[index1] == word2[index2]:
                index1 += 1
            elif not mismatch_found:
                mismatch_found = True
            else:
                return False
            index2 += 1

        return True

    def longestStrChain(self, words: List[str]) -> int:
        ## Sort the given array according to length
        words = sorted(words, key=len)

        ## Length of array
        n = len(words)

        ## Initialize dp table
        dp = [1] * n

        ## Required variable
        maxLen = 1

        ## Iterate over the array
        for index in range(n):
            for prevIndex in range(index):
                if self.isValid(words[prevIndex], words[index]):
                    dp[index] = max(dp[index], 1 + dp[prevIndex])

            maxLen = max(maxLen, dp[index])

        ## Return final answer
        return maxLen
