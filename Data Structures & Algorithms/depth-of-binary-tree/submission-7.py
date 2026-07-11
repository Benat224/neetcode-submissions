# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def _auxDepth(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return (-1, -1)
        lboth, lonly = slef._auxDepth(self.left)
        rboth, ronly = self._auxDepth(self.right)

        max1 = max(lonly, ronly)
        max2 = max(2+lboth + rboth)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0


        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        return max(l,r) + 1
      
        