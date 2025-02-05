class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create adjacency list
        adj = [[] for _ in range(n)]
        for u, v, dist in flights:
            adj[u].append((v, dist))

        # Initialise distance array
        distances = [float('inf')] * n

        # Initilise queue for BFS
        q = deque()
        q.append((0, src, 0)) # (stops, node, distance)
        distances[src] = 0 

        while q:
            stops, node, curr_dist = q.popleft()
            # Continue if we reach max stops and not the destination
            if stops == k+1 and node != dst:
                continue

            for neighbor, dist in adj[node]:
                new_dist = curr_dist + dist
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    q.append((stops+1, neighbor, new_dist))

        # Return -1 if destination cannot be reached
        if distances[dst] == float('inf'):
            return -1
        else:
            return distances[dst]
