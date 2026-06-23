# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.answer = []
        self.backTrack(root, targetSum, [])
        return self.answer

    def backTrack(self, root: Optional[TreeNode], sum: int, curr: List[int]):
        if root is None:
            return

        if root.left is None and root.right is None:
            if sum == root.val:
                curr.append(root.val)
                self.answer.append(curr.copy())
                curr.pop()
            return

        curr.append(root.val)

        self.backTrack(root.left, sum - root.val, curr)
        self.backTrack(root.right, sum - root.val, curr)

        curr.pop()