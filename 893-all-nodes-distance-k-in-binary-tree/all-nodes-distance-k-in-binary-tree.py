from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int):
        # Step 1: Build graph (undirected)
        graph = defaultdict(list)

        def build_graph(node, parent):
            if node:
                if parent:
                    graph[node.val].append(parent.val)
                    graph[parent.val].append(node.val)
                build_graph(node.left, node)
                build_graph(node.right, node)

        build_graph(root, None)

        # Step 2: BFS from target node
        visited = set()
        queue = deque([(target.val, 0)])
        res = []

        while queue:
            node, dist = queue.popleft()
            if node in visited:
                continue
            visited.add(node)

            if dist == k:
                res.append(node)
            elif dist < k:
                for neighbor in graph[node]:
                    queue.append((neighbor, dist + 1))

        return res
