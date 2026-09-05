class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        for u, v in edges:
            root_u = find(u)
            root_v = find(v)

            if root_u == root_v:
                return [u, v]

            parent[root_u] = root_v

        return []
        