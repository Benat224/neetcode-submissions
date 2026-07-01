# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        level = 1
        maxi = 1
        if not root:
            return 0
        queue = deque([(root, level)])
        # queue.append()
        while queue:
            cur = queue.popleft()
            maxi = max(maxi, cur[1])
            if cur[0].left:
                queue.append([cur[0].left, cur[1] + 1])
            if cur[0].right:
                queue.append([cur[0].right, cur[1] + 1])
        return maxi