class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # Map original nodes to their copies
        old_to_new = {}

        # Create a copy of every node
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # Connect next and random pointers
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next

        return old_to_new[head]