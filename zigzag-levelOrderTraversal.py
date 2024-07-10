"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
"""
def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    dir = True
    queue = collections.deque()
    queue.append(root)
    ans = []
    while len(queue) > 0:
        ans.append([])
        length = len(queue)
        for i in range(length):
            if dir:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                node = queue.pop()
                if node.right:
                    queue.appendleft(node.right)
                if node.left:
                    queue.appendleft(node.left)
            ans[-1].append(node.val)
        dir = not dir
    return ans