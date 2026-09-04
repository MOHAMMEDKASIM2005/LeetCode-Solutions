class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        safe = {}

        def dfs(i):
            # Already visited
            if i in safe:
                return safe[i]

            # Assume unsafe first
            safe[i] = False

            # Check every neighbour
            for nei in graph[i]:
                if not dfs(nei):
                    return safe[i]

            # All neighbours are safe
            safe[i] = True
            return safe[i]

        res = []

        for i in range(n):
            if dfs(i):
                res.append(i)

        return res