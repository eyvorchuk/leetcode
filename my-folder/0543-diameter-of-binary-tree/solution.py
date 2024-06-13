# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is None:
                return (0,0)
            height_left, diameter_left = height(root.left)
            height_right, diameter_right = height(root.right)
            diameter = height_left + height_right
            return (1+max(height_left, height_right), max(diameter, diameter_left, diameter_right))
        return height(root)[1]
