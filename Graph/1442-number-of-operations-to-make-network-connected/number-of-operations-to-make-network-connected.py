class Solution:
    def dfs(self, node, visited, adj):
        # Visit the node
        visited[node] = 1

        # Call dfs for all adjacent unvisited nodes
        for neighbor in adj[node]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, adj)

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #*********** Using Traversal *************#
        
        # Return if number of edges is less than number of nodes-1
        if len(connections) < n-1:
            return -1

        # Create adjacency list for dfs
        adj = [[] for _ in range(n)]
        for u, v, in connections:
            adj[u].append(v)
            adj[v].append(u)

        # Visitied array to keep track of visited nodes
        visited = [0 for _ in range(n)]

        # Count number of islands using dfs
        count = 0
        for node in range(n):
            if not visited[node]:
                self.dfs(node, visited, adj)
                count += 1

        # Return number of operations needed
        return count-1

