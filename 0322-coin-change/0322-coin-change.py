class Solution:
    def coinChange(self, coins, amount):

        # dp[i] = minimum coins needed to make i
        dp = [amount + 1] * (amount + 1)

        # 0 coins are needed to make 0
        dp[0] = 0

        # Check every amount
        for i in range(1, amount + 1):

            # Try every coin
            for coin in coins:

                # Only use the coin if it fits
                if coin <= i:

                    # Take the smaller answer
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If impossible, return -1
        if dp[amount] == amount + 1:
            return -1

        return dp[amount]