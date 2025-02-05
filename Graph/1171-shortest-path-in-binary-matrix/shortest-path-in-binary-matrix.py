class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # If start or end cell is blocked
        if grid[0][0] == 1 or grid[m-1][n-1] == 1:
            return -1

        distances = [[float('inf')] * n for _ in range(m)]

        q = deque()
        q.append((0, 0))
        distances[0][0] = 1

        while q:
            row, col = q.popleft()

            if row == m-1 and col == n-1:
                return distances[row][col]

            for delrow in range(-1, 2):
                for delcol in range(-1, 2):
                    new_row = row + delrow
                    new_col = col + delcol

                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 0:
                        new_dist = distances[row][col] + 1
                        if(distances[new_row][new_col] > new_dist):
                            distances[new_row][new_col] = new_dist
                            q.append((new_row, new_col))

        return -1  