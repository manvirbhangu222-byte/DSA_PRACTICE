# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        result=[]
        def dfs(node):
            if node is None:
                result.append("#")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(result)
    def deserialize(self, data):
        values=data.split(",")
        index=0
        def dfs():
            nonlocal index
            if values[index]=="#":
                index +=1
                return
            node=TreeNode(int(values[index]))
            index +=1

            node.left=dfs()
            node.right=dfs()
            return node
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))