class Solution:
    def isValidBST(self, root):
        def validate(node, low, high):
            if node is None:
                return True

            # Current node must be strictly within the allowed range
            if not (low < node.val < high):
                return False

            # Left: values must be smaller than node.val
            # Right: values must be greater than node.val
            return (
                validate(node.left, low, node.val)
                and validate(node.right, node.val, high)
            )

        return validate(root, float("-inf"), float("inf"))