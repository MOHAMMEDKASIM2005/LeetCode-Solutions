class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for c in num:
            while k > 0 and stack and stack[-1] > c:
                stack.pop()
                k -= 1

            stack.append(c)

        # If k digits are still left, remove them from the end
        if k > 0:
            stack = stack[:-k]

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else "0"