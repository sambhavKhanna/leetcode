"""
Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""

def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    def leaf_value_sequence(root: Optional[TreeNode]):
        if not root.left and not root.right:
            return [root.val]
        elif not root.left:
            return leaf_value_sequence(root.right)
        elif not root.right:
            return leaf_value_sequence(root.left)
        else:
            left_part = leaf_value_sequence(root.left)
            right_part = leaf_value_sequence(root.right)
            left_part.extend(right_part)
            return left_part
    arr1 = leaf_value_sequence(root1)
    arr2 = leaf_value_sequence(root2)
    print(arr1)
    print(arr2)
    p1, p2 = 0, 0
    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] != arr2[p2]:
            return False
        p1 += 1
        p2 += 1
    return len(arr1) == len(arr2)