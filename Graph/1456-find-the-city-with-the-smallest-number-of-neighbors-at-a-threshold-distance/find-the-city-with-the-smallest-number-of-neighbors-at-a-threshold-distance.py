from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], tresh: int) -> int:
        ############### Using Floyd Warshall #################
        INF = float('inf')
        # Create adjacency matrix
        adjMat = [[INF] * n for _ in range(n)]

        for i in range(n):
            adjMat[i][i] = 0
        
        for u, v, wt in edges:
            adjMat[u][v] = wt
            adjMat[v][u] = wt

        # Apply Floyd Warshall
        for via in range(n):
            for u in range(n):
                for v in range(n):
                    # If u to via and via to v are not INF
                    if adjMat[u][via] != INF and adjMat[via][v] != INF:
                        adjMat[u][v] = min(adjMat[u][v], adjMat[u][via] + adjMat[via][v])

        # Find the required city
        answerCity = -1
        answerCnt = n  

        for u in range(n):
            temp_cnt = sum(1 for v in range(n) if u != v and adjMat[u][v] <= tresh)

            if temp_cnt <= answerCnt:
                answerCnt = temp_cnt
                answerCity = u

        return answerCity
