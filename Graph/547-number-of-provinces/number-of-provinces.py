class Solution:
    def dfs(self, node, isConnected, visited, num_nodes):
        visited[node] = 1

        for i in range(num_nodes):
            if not visited[i] and isConnected[node][i] == 1:
                self.dfs(i, isConnected, visited, num_nodes)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        num_nodes = len(isConnected)
        visited = [0] * (num_nodes+1)

        for i in range(num_nodes):
            if not visited[i]:
                count += 1
                self.dfs(i, isConnected, visited, num_nodes)

        return count