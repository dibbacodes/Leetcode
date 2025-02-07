from collections import deque
from typing import List

class Solution:
    def isValidCell(self, row, col, len_rows, len_cols):
        return 0 <= row < len_rows and 0 <= col < len_cols  # Fixed `len_cols`

    def orangesRotting(self, grid: List[List[int]]) -> int:
        len_rows = len(grid)
        len_cols = len(grid[0])

        q = deque()
        fresh_count = 0
        time = 0

        # Step 1: Identify initial rotten oranges and count fresh ones
        for row in range(len_rows):
            for col in range(len_cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0  # No fresh oranges to rot

        # Directions for moving in 4 directions (up, left, down, right)
        delrow = [-1, 0, 1, 0]
        delcol = [0, -1, 0, 1]
        
        # Step 2: BFS Processing
        while q:
            size = len(q)
            made_change = False  # Track if we rotted any orange in this round

            for _ in range(size):
                row, col = q.popleft()

                for i in range(4):
                    nrow = row + delrow[i]
                    ncol = col + delcol[i]

                    if self.isValidCell(nrow, ncol, len_rows, len_cols) and grid[nrow][ncol] == 1:
                        q.append((nrow, ncol))
                        grid[nrow][ncol] = 2  # Mark orange as rotten
                        fresh_count -= 1
                        made_change = True

            if made_change:  # Increment time only if at least one orange got rotted
                time += 1

        return time if fresh_count == 0 else -1  # If there are still fresh oranges, return -1
