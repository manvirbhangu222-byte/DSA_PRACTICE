# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder, inorder):

        inorder_map = {}

        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i

        preorder_index = 0

        def build(left, right):
            nonlocal preorder_index

            if left > right:
                return None

            root_value = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(root_value)

            root_index = inorder_map[root_value]

            root.left = build(left, root_index - 1)
            root.right = build(root_index + 1, right)

            return root

        return build(0, len(inorder) - 1)
        