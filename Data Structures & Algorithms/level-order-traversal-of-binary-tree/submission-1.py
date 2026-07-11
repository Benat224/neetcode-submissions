# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = []
        res = []
        height = 0
        if not root:
            return res
        stack.append((root, height))
        while stack:
            cur, level = stack.pop()
            if len(res) < level+1:
                res.append([])
               
            res[level].append(cur.val)

            if cur.right:
                stack.append((cur.right, level+1))
            if cur.left:
                stack.append((cur.left, level+1))

        return res
        
        # queue = deque([root])
        # res = []
        # if not root:
        #     return res
        # while queue:
        #     local = []
        #     for _ in range(len(queue)):
        #         cur = queue.popleft()
        #         local.append(cur.val)
        #         if cur.left:
        #             queue.append(cur.left)
        #         if cur.right:
        #             queue.append(cur.right)
        #     res.append(local)
        # return res