# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        path=[]
        result=[]
        def dfs(node, remaining):
            if node is None:
                return 
            path.append(node.val)
            remaining-=node.val

            if node.left is None and node.right is None:
                if remaining==0:
                    result.append(path[:])
            else:
                dfs(node.left,remaining)
                dfs(node.right,remaining)
            path.pop()
        dfs(root,targetSum)

        return result
       
        