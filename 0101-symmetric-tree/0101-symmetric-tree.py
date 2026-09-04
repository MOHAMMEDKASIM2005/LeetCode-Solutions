class Solution:
    def isSymmetric(self, root):

        def check(left, right):

            if left == None and right == None:
                return True

            if left == None or right == None:
                return False

            if left.val != right.val:
                return False

            return check(left.left, right.right) and check(left.right, right.left)

        return check(root.left, root.right)