"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.
"""

def maxPathSum(self, root: Optional[TreeNode]) -> int:
    def recur(root):
        if not root:
            return (0, -1001)
        right_sum, right_max = recur(root.right)
        left_sum, left_max = recur(root.left)
        if left_sum < 0:
            left_sum = 0
        if right_sum < 0:
            right_sum = 0
        tree_sum = left_sum + right_sum + root.val
        max_so_far = max(tree_sum, right_max, left_max)
        return_sum = max(left_sum, right_sum) + root.val
        return (return_sum, max_so_far)
    total_sum, ans = recur(root)
    return ans