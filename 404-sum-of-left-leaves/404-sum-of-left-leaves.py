# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode],isLeft=True) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val if not isLeft else 0
        return self.sumOfLeftLeaves(root.right,True)+self.sumOfLeftLeaves(root.left,False)