# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = []
        stack.append(root)
        mini, maxi = min(p.val,q.val), max(p.val,q.val)
        while stack:
            cur = stack.pop()
            if cur.val >= mini and cur.val <= maxi:
                return cur
            if cur.val < mini:
                stack.append(cur.right)
            else:
                stack.append(cur.left)
        
        
        
        mini, maxi = min(p.val,q.val), max(p.val,q.val)
        if mini <= root.val and maxi >= root.val:
            return root
        if maxi < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)
