class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            # Find the kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next

                if not kth:
                    return dummy.next

            group_next = kth.next

            # Reverse the group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Connect the reversed group
            old_first = group_prev.next
            group_prev.next = kth

            # old_first is now the last node of the reversed group
            group_prev = old_first