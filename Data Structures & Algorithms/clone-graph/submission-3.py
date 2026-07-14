"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mp = defaultdict(set)
        total = defaultdict(Node)
        def dfs(copy_node, real_node):
            for neigh in real_node.neighbors:
                explore = False
                if not neigh.val in mp[copy_node.val]:
                    print(real_node.val)
                    print(neigh.val)
                    if not neigh.val in total:
                        print(f'New:{neigh.val}')
                        new = Node(neigh.val)
                        total[neigh.val] = new
                        explore = True
                
                    new = total[neigh.val]
                    copy_node.neighbors.append(new)
                    mp[copy_node.val].add(new.val)
                    if explore:
                        dfs(new, neigh)
                
        if not node:
            return node

        root = Node(val = node.val)
        total[node.val] = root
        dfs(root, node)
        return root

