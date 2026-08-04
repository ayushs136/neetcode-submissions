class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        q = deque()
        for r in range(row):
            for c in range(col):
                if (r == 0 or c == 0 or r == row - 1 or c == col - 1) and board[r][
                    c
                ] == "O":
                    q.append((r, c))
                    board[r][c] = "#"

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while q:

            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < row and 0 <= nc < col and board[nr][nc] == "O":
                    board[nr][nc] = "#"
                    q.append((nr, nc))

        for r in range(row):
            for c in range(col):

                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "#":
                    board[r][c] = "O"
