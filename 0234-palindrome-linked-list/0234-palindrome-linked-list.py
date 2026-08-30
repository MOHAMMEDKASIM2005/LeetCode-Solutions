class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # 1. Find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse the second half
        prev = None

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # prev is now the head of the reversed second half
        right = prev
        left = head

        # 3. Compare both halves
        while right:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True