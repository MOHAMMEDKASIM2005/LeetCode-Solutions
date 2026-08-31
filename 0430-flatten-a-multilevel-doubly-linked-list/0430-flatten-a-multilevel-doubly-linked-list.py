class Solution:
    def flatten(self, head):
        if not head:
            return head

        curr = head

        while curr:
            if curr.child:
                child = curr.child
                next_node = curr.next

                # Flatten the child list first
                child_tail = child
                while child_tail.next:
                    child_tail = child_tail.next

                # Insert child list between curr and next_node
                curr.next = child
                child.prev = curr

                if next_node:
                    child_tail.next = next_node
                    next_node.prev = child_tail

                # Child pointer must be removed
                curr.child = None

            curr = curr.next

        return head
        