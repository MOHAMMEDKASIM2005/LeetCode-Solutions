class Solution:
    def detectCycle(self, head):
        slow = head
        fast = head

        # Step 1: Detect if a cycle exists
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Step 2: Find the node where the cycle begins
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow