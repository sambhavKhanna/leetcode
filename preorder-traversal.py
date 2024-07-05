"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.
"""
def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return root
    stack = [root]
    ans = []
    while len(stack) > 0:
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        ans.append(node.val)
    return ans