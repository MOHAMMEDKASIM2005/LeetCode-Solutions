from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):

        # Create graph
        graph = [[] for _ in range(numCourses)]

        # Count prerequisites
        indegree = [0] * numCourses

        # Build graph
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        # Put courses with no prerequisites into queue
        queue = deque()

        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        # Store answer
        result = []

        # Process courses
        while queue:

            course = queue.popleft()
            result.append(course)

            # Remove this course as a prerequisite
            for next_course in graph[course]:

                indegree[next_course] -= 1

                # All prerequisites completed
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # If all courses are completed
        if len(result) == numCourses:
            return result

        # Cycle exists
        return []