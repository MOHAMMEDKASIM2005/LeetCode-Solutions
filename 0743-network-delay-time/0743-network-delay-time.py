class Solution:
    def networkDelayTime(self, times, n, k):
        dist = [float('inf')] * (n + 1)

        dist[k] = 0

        # Relax all edges n - 1 times
        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        answer = 0

        # Find the longest shortest-path distance
        for i in range(1, n + 1):
            if dist[i] == float('inf'):
                return -1

            answer = max(answer, dist[i])

        return answer