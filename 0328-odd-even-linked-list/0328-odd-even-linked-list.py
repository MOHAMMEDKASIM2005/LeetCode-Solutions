class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            # Connect current odd node to the next odd node
            odd.next = even.next
            odd = odd.next

            # Connect current even node to the next even node
            even.next = odd.next
            even = even.next

        # Attach even list after odd list
        odd.next = even_head

        return head