class Solution:
    def invertTree(self, root):

        if root is None:
            return None

        # Swap left and right
        root.left, root.right = root.right, root.left

        # Invert left subtree
        self.invertTree(root.left)

        # Invert right subtree
        self.invertTree(root.right)

        return root