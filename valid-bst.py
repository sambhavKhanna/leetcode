"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""

def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def recur(root):
        if not root:
            return (True, True, 0, 0)
        check_left, left_is_null, max_left, min_left = recur(root.left)
        check_right, right_is_null ,max_right, min_right = recur(root.right)
        if left_is_null:
            max_left = root.val
            min_left = root.val
        if right_is_null:
            max_right = root.val
            min_right = root.val
        check = check_left and check_right and ((root.val > max_left) or left_is_null) and ((root.val < min_right) or right_is_null)
        if not check:
            return (False, False, 0, 0)
        return (True, False, max_right, min_left)
    ans, is_null, max_val, min_val = recur(root)
    return ans