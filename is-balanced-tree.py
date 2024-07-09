"""
Given a binary tree, determine if it is height-balanced.
"""

def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def height_of_tree(root):
        if not root:
            return (0, True)
        ans = True
        left_height, ans_left = height_of_tree(root.left)
        right_height, ans_right = height_of_tree(root.right)
        if abs(left_height - right_height) > 1:
            ans = False
        else:
            ans = ans_left and ans_right
        height = 1 + max(left_height, right_height)
        return (height, ans)
    height, ans = height_of_tree(root)
    return ans