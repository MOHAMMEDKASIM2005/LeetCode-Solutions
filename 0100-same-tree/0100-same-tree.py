class Solution:
    def isSameTree(self, p, q):
        # Both nodes are empty
        if not p and not q:
            return True

        # One is empty, or values are different
        if not p or not q or p.val != q.val:
            return False

        # Compare left and right subtrees
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )