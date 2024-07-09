"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.
"""

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    st1 = [root]
    st2 = []
    while len(st1) > 0:
        node = st1.pop()
        if node.left:
            st1.append(node.left)
        if node.right:
            st1.append(node.right)
        st2.append(node.val)
    st2.reverse()
    return st2