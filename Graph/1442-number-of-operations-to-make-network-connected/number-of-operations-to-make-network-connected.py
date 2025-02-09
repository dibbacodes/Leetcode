class DisjointSet:
    # Funtion to declare instance of DisjointSet Class
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.parent = [node for node in range(num_nodes)]
        self.size = [1 for _ in range(num_nodes)]

    # Funtion to find Ultimate Parent of node
    def findUPar(self, node):
        if self.parent[node] == node:
            return node
        else:
            # Path compression
            self.parent[node] = self.findUPar(self.parent[node])
            return self.parent[node]

    # Funtion to Join 2 Nodes
    def unionBySize(self, u, v):
        ultPar_u = self.findUPar(u)
        ultPar_v = self.findUPar(v)

        # Return if u and v already in same set of nodes
        if ultPar_u == ultPar_v:
            return 

        # Union By Size
        if self.size[ultPar_u] < self.size[ultPar_v]:
            self.parent[ultPar_u] = ultPar_v
            self.size[ultPar_v] += self.size[ultPar_u]
        else:
            self.parent[ultPar_v] = ultPar_u
            self.size[ultPar_u] += self.size[ultPar_v]

    
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ########## USING DISJOINT SET DATA STRUCTURE ##############

        # Declare a Disjoint class instance
        ds = DisjointSet(n)

        # Count extra edges
        extraEdges = 0
        for u, v in connections:
            if ds.findUPar(u) == ds.findUPar(v):
                extraEdges += 1
            else:
                ds.unionBySize(u, v) 

        # Count number of components
        components = 0
        for node in range(n):
            if ds.parent[node] == node:
                components += 1

        # Return conditions
        if components-1 <= extraEdges:
            return components-1
        else:
            return -1