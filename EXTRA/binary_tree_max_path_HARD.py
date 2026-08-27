class treeNode(object):
    def __init__(self,val,left,right):
        self.val=val
        self.left=left
        self,right=right
class Solution():
    def maxPathSum(self,root):
        max_sum=float("-inf")
        def dfs(node):
            nonlocal max_sum
            if node is None:
                return 0
            left_gain=max(0,dfs(node.left))
            right_gain=max(0,dfs(node.right))
            
            current_path=(left_gain +right_gain+node.val)
            
            max_sum=max(max_sum,current_path)
            return node.val + max(left_gain,right_gain)
        dfs(root)
        return max_sum
