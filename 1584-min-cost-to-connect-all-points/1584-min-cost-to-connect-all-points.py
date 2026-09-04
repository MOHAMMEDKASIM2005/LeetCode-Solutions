class Solution:

    def minCostConnectPoints(self, points):

        n = len(points)

        visited = [False] * n
        distance = [float('inf')] * n

        distance[0] = 0
        total = 0

        for step in range(n):

            # Find nearest unvisited point
            cur = -1

            for i in range(n):

                if visited[i] == False:

                    if cur == -1 or distance[i] < distance[cur]:
                        cur = i

            # Connect the point
            visited[cur] = True
            total = total + distance[cur]

            # Update distances
            for i in range(n):

                if visited[i] == False:

                    x = abs(points[cur][0] - points[i][0])
                    y = abs(points[cur][1] - points[i][1])

                    cost = x + y

                    if cost < distance[i]:
                        distance[i] = cost

        return total


# Input
points = [[3,12],[-2,5],[-4,1]]

# Create object
obj = Solution()

# Call function
answer = obj.minCostConnectPoints(points)

# Print answer
print(answer)