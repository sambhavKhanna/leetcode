"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    ans = []
    queue = collections.deque()
    queue.append(root)
    while len(queue) > 0:
        length = len(queue)
        vals = []
        for i in range(length):
            node = queue.popleft()
            vals.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        ans.append(vals)
    return ans