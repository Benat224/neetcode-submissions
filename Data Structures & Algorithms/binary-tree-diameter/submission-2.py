# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def _auxDepth(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return (0, 0)
        
        lboth, lonly = self._auxDepth(root.left)
        rboth, ronly = self._auxDepth(root.right)

        counter = 0
        if root.left:
            counter += 1
        if root.right:
            counter += 1

        max1 = max(lonly, ronly, counter + lboth + rboth )

        max2 = max(lboth,rboth)+ (counter + 1)//2

        return max2, max1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        result =  self._auxDepth(root)
        return max(result[0], result[1])