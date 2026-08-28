class Solution:
    def partition(self, s):
        result = []
        path = []

        def isPalindrome(string):
            return string == string[::-1]

        def backtrack(start):

            # Base case
            if start == len(s):
                result.append(path[:])
                return

            # Try every possible substring
            for end in range(start + 1, len(s) + 1):

                substring = s[start:end]

                # Only continue if palindrome
                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(end)
                    path.pop()

        backtrack(0)

        return result


sol = Solution()
s = "aab"
print(sol.partition(s))