class Solution(object):
    def gardenNoAdj(self, n, paths):
        graph = [[] for i in range(n)]

        for a, b in paths:
            graph[a-1].append(b-1)
            graph[b-1].append(a-1)

        ans = [0] * n

        for i in range(n):
            used = set()

            for j in graph[i]:
                if ans[j] != 0:
                    used.add(ans[j])

            for flower in range(1, 5):
                if flower not in used:
                    ans[i] = flower
                    break

        return ans