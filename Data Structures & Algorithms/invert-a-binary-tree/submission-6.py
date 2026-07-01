# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # BFS
        # queue = deque([root])
        # if not root:
        #     return root
        # while queue:
        #     cur = queue.popleft()
        #     cur.left, cur.right = cur.right, cur.left
        #     if cur.left:
        #         queue.append(cur.left)
        #     if cur.right:
        #         queue.append(cur.right)
        # return root


        # BFS (Preorder traversal) recursive
        # if not root: return root

        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        # BFS iterative

        stack = []
        if not root: return root
        stack.append(root)
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return root
