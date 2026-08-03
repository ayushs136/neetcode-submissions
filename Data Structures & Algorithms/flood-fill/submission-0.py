class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])

        q = deque([(sr, sc)])
        oldColor = image[sr][sc]

        if oldColor == color:
            return image
        image[sr][sc] = color

        delRow = [-1, 0, 1, 0]
        delCol = [0, 1, 0, -1]

        while q:
            r, c = q.popleft()

            for i in range(4):
                nrow = r + delRow[i]
                ncol = c + delCol[i]

                if 0 <= nrow < rows and 0 <= ncol < cols and image[nrow][ncol] == oldColor:
                    q.append((nrow, ncol))
                    image[nrow][ncol] = color

        return image
