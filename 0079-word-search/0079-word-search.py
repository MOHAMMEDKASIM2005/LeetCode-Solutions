class Solution:

    def exist(self, board, word):
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if self.dfs(board, word, i, j, 0):
                    return True

        return False

    def dfs(self, board, word, row, col, index):

        # Word is completely matched
        if index == len(word):
            return True

        # Out of bounds
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return False

        # Current character doesn't match
        if board[row][col] != word[index]:
            return False

        # Mark the cell as visited
        temp = board[row][col]
        board[row][col] = '#'

        # Check all 4 directions
        found = (
            self.dfs(board, word, row + 1, col, index + 1) or  # down
            self.dfs(board, word, row - 1, col, index + 1) or  # up
            self.dfs(board, word, row, col + 1, index + 1) or  # right
            self.dfs(board, word, row, col - 1, index + 1)     # left
        )

        # Restore the cell (backtracking)
        board[row][col] = temp

        return found