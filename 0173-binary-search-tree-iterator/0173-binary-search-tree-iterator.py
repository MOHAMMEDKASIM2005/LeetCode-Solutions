class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        # The top of the stack is the next smallest element
        node = self.stack.pop()

        # After visiting this node, process its right subtree
        if node.right:
            self._push_left(node.right)

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0