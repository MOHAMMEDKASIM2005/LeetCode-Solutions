class Solution:
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)

        # Not enough flowers to make m bouquets
        if m * k > n:
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        def can_make(day):
            bouquets = 0
            flowers = 0

            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1

                    # k adjacent bloomed flowers -> 1 bouquet
                    if flowers == k:
                        bouquets += 1
                        flowers = 0

                        if bouquets >= m:
                            return True
                else:
                    # Adjacency is broken
                    flowers = 0

            return False

        while left < right:
            mid = (left + right) // 2

            if can_make(mid):
                right = mid
            else:
                left = mid + 1

        return left