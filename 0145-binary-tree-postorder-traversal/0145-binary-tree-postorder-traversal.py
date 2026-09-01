from typing import Optional, List

class Solution:
    def postorderTraversal(self, root: Optional['TreeNode']) -> List[int]:
        if not root:
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)

            # Push left first, then right.
            # Right will be popped first.
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result[::-1]