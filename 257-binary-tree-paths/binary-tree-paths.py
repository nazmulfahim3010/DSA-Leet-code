# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        result =[]

        def dfs(node,sol):
            if not node:
            
                return

            sol.append(str(node.val))
            
            if not node.left and not node.right:
                result.append("->".join(sol))

            

            dfs(node.left,sol)
            dfs(node.right,sol)

            sol.pop()

        dfs(root,[])
        return result

            
        