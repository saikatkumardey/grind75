# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return root
        
        if root.left is None and root.right is None:
            return root
        
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        root.left, root.right = right_inverted, left_inverted
        
        return root
        