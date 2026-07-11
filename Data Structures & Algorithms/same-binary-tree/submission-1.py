# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q or not p and q:
            return False

        stack1, stack2 = [], []
        stack1.append(p)
        stack2.append(q)

        while stack1 and stack2:
            valp, valq = stack1.pop(), stack2.pop()
            if not valp and not valq:
                continue
            if valp and not  valq or not valp and valq or valp.val != valq.val:
                return False
            
            stack1.append(valp.right)
            stack2.append(valq.right)
            stack1.append(valp.left)
            stack2.append(valq.left)
        return True

        
        
        
        
        if not p and not q:
            return True
        if not p and q or p and not q:
            return False
        valp, valq = p.val, q.val
        if valp != valq:
            return False

        return  self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
