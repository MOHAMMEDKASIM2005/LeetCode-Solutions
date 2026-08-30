class Solution:
    def isValid(self, s):
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in pairs:
                # Closing bracket
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                # Opening bracket
                stack.append(char)

        # Valid only if there are no unmatched opening brackets
        return len(stack) == 0