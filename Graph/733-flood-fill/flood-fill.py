from collections import deque
class Solution:
    def isValid(self, row, col, m, n):
        if 0 <= row < m and 0 <= col < n:
            return True
        
        return False

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])

        q = deque()
        q.append((sr, sc))
        original_color = image[sr][sc]
        image[sr][sc] = color

        if original_color == color:  
            return image

        delrow = [1, 0, -1, 0]
        delcol = [0, 1, 0, -1]

        while q:
            row, col = q.popleft()

            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]

                if self.isValid(nrow, ncol, m, n) and image[nrow][ncol] == original_color:
                    q.append((nrow, ncol))
                    image[nrow][ncol] = color

        return image