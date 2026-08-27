class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        current = head

        while current:
            # Save the next node before changing current.next
            next_node = current.next

            # Find where current belongs
            prev = dummy
            while prev.next and prev.next.val < current.val:
                prev = prev.next

            # Insert current into the sorted part
            current.next = prev.next
            prev.next = current

            current = next_node

        return dummy.next