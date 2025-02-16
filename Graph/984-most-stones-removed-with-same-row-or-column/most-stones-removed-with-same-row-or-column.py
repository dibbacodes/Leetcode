from collections import defaultdict

class DisjointSet:
    def __init__(self, num_nodes):
        self.parent = [node for node in range(num_nodes)]
        self.size = [1 for _ in range(num_nodes)]

    def findUPar(self, node):
        if self.parent[node] == node:
            return node
        else:
            self.parent[node] = self.findUPar(self.parent[node])
            return self.parent[node]

    def UnionBySize(self, u, v):
        Upar_u = self.findUPar(u)
        Upar_v = self.findUPar(v)

        if Upar_u == Upar_v:
            return 

        if self.size[Upar_u] < self.size[Upar_v]:
            self.parent[Upar_u] = self.parent[Upar_v]
            self.size[Upar_v] += self.size[Upar_u]

        else:
            self.parent[Upar_v] = self.parent[Upar_u]
            self.size[Upar_u] += self.size[Upar_v]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        maxRowIndex = 0
        maxColIndex = 0

        n = len(stones)

        for row, col in stones:
            maxRowIndex = max(row, maxRowIndex)
            maxColIndex = max(col, maxColIndex)

        ds = DisjointSet(maxRowIndex + maxColIndex + 2)
        stonePresent = {}

        for row, col in stones:
            rowNode = row
            colNode = col + maxRowIndex + 1
            
            ds.UnionBySize(rowNode, colNode)

            stonePresent[rowNode] = 1
            stonePresent[colNode] = 1

        componentCounts = 0
        for node in stonePresent:
            if ds.findUPar(node) == node:
                componentCounts += 1

        return n - componentCounts