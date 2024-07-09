"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""
def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def height_of_tree(root):
        if not root:
            return (0, 0)
        left_height, max_left = height_of_tree(root.left)
        right_height, max_right = height_of_tree(root.right)
        diameter = left_height + right_height
        cur_diameter = max(diameter, max_left, max_right)
        height = 1 + max(left_height, right_height)
        return (height, cur_diameter)
    height, ans = height_of_tree(root)
    return ans