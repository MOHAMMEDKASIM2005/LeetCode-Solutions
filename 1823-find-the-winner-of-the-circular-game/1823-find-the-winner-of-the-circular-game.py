class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0

        for friends in range(2, n + 1):
            winner = (winner + k) % friends

        return winner + 1