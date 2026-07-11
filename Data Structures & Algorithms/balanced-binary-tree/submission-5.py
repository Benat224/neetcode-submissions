# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(root:Optional[TreeNode]) -> int:
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            if l == -1 or r == -1 or abs(l-r) > 1:
                return -1
            return max(l,r) + 1
        
        if not root:
            return True
        visited = defaultdict(int)
        stack = []
        stack.append(root)
        while stack:
            cur = stack[-1]
            if cur.left and cur.left not in visited:
                stack.append(cur.left)
            elif cur.right and cur.right not in visited:
                stack.append(cur.right)
            else:
                cur = stack.pop()
                if abs(visited[cur.left]-visited[cur.right]) > 1:
                    return False
                visited[cur] = max(visited[cur.left], visited[cur.right])+1
        return True
        return height(root) != -1