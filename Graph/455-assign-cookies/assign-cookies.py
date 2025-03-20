class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        ###### GREEEDY ######

        ## Sort the greed and size array
        greed = sorted(g)
        size = sorted(s)
        
        count = 0
        i = 0
        j = 0
        coutn = 0
        while i < len(greed) and j < len(size):
            if greed[i] <= size[j]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1

        return count


