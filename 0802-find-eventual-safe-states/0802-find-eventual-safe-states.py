from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)

        # Reverse graph:
        # rev[v] contains all nodes that point to v.
        rev = [[] for _ in range(n)]

        # out_degree[i] = number of outgoing edges from i
        out_degree = [len(graph[i]) for i in range(n)]

        for u in range(n):
            for v in graph[u]:
                rev[v].append(u)

        # Terminal nodes have out_degree == 0
        q = deque(i for i in range(n) if out_degree[i] == 0)

        safe = [False] * n

        while q:
            node = q.popleft()
            safe[node] = True

            # Any predecessor loses one "unsafe" outgoing edge.
            for prev in rev[node]:
                out_degree[prev] -= 1

                # All outgoing neighbors of prev are now safe.
                if out_degree[prev] == 0:
                    q.append(prev)

        # Iterating in index order guarantees ascending order.
        return [i for i in range(n) if safe[i]]