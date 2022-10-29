# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def height(node):
            
            if node is None:
                return 0, True
            
            left_height, left_balanced = height(node.left)
            right_height, right_balanced = height(node.right)
            
            if not left_balanced or not right_balanced:
                return 0, False
            
            if abs(left_height - right_height) > 1:
                return 0, False
            
            return 1 + max(left_height, right_height), True
        
        
        _, is_balanced = height(root)
        
        return is_balanced