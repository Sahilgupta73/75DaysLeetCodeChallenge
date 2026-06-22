# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        pathP = []
        self.path(root, p, pathP)

        pathQ = []
        self.path(root, q, pathQ)

        ans = None
        i = 0

        while i < len(pathP) and i < len(pathQ) and pathP[i] == pathQ[i]:
            ans = pathP[i]
            i += 1

        return ans

    def path(self, root, target, curr):
        if root is None:
            return False

        curr.append(root)

        if root == target:
            return True

        if self.path(root.left, target, curr) or \
           self.path(root.right, target, curr):
            return True

        curr.pop()
        return False   