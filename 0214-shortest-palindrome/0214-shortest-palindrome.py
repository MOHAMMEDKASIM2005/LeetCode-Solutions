class Solution:
    def shortestPalindrome(self, s):
        if not s:
            return ""

        rev = s[::-1]
        combined = s + "#" + rev

        # Build KMP prefix table
        lps = [0] * len(combined)

        for i in range(1, len(combined)):
            j = lps[i - 1]

            while j > 0 and combined[i] != combined[j]:
                j = lps[j - 1]

            if combined[i] == combined[j]:
                j += 1

            lps[i] = j

        # Length of the longest palindromic prefix
        palindrome_length = lps[-1]

        # Characters after the palindromic prefix
        remaining = s[palindrome_length:]

        return remaining[::-1] + s