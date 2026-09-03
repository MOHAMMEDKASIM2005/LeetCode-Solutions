class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


            count = {}

            # Count each task
            for task in tasks:
                if task in count:
                    count[task] += 1
                else:
                    count[task] = 1

            # Find maximum frequency
            max_count = max(count.values())

            # Count how many tasks have maximum frequency
            max_tasks = 0

            for value in count.values():
                if value == max_count:
                    max_tasks += 1

            # Calculate minimum time
            part = (max_count - 1) * (n + 1) + max_tasks

            answer = max(len(tasks), part)

            return answer
        