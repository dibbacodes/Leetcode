class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7 
        # Create adjacency list
        adj = defaultdict(list)
        for u, v, wt in roads:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        # Initialise times and ways array
        times = [float('inf')] * n
        ways = [0] * n

        # Initialise Min-Heap
        pq = [(0, 0)] # (time, node)
        times[0] = 0
        ways[0] = 1

        while pq:
            time, node = heapq.heappop(pq)

            for neighbor, wt in adj[node]:
                new_time = time + wt
                if new_time < times[neighbor]:
                    times[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))
                    ways[neighbor] = ways[node]
                
                elif new_time == times[neighbor]:
                    ways[neighbor] = (ways[node] + ways[neighbor]) % MOD

        return ways[n-1] 