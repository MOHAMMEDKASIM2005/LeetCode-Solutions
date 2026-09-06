class Solution:
    def minScoreTriangulation(self, values: list[int]) -> int:
        n = len(values)

        # dp[i][j] = minimum score to triangulate
        # the polygon from vertex i to vertex j.
        dp = [[0] * n for _ in range(n)]

        # length is the distance between i and j
        # We need at least 2 edges, i.e. 3 vertices.
        for length in range(2, n):
            for i in range(n - length):
                j = i + length

                dp[i][j] = float('inf')

                # Choose k as the third vertex of triangle (i, k, j)
                for k in range(i + 1, j):
                    score = (
                        dp[i][k]
                        + dp[k][j]
                        + values[i] * values[k] * values[j]
                    )

                    dp[i][j] = min(dp[i][j], score)

        return dp[0][n - 1]
