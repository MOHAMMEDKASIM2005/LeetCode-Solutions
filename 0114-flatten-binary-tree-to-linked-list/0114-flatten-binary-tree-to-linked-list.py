class Solution:
    def flatten(self, root):
        cur = root

        while cur:
            if cur.left:
                # Find the rightmost node in the left subtree
                pred = cur.left
                while pred.right:
                    pred = pred.right

                # Connect original right subtree after the left subtree
                pred.right = cur.right

                # Move left subtree to the right
                cur.right = cur.left
                cur.left = None

            # Move to the next node in the flattened list
            cur = cur.right