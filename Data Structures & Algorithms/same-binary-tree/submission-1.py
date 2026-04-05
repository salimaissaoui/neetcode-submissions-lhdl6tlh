# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS through p and q, for each iteration of dfs, append the value to a list. If the lists are not the same, return false. If the lists are the same, return true.
        vals1 = []
        vals2 = []
        def dfs(root, values):
            if not root:
                return values.append(None)
            values.append(root.val)
            dfs(root.left, values)
            dfs(root.right, values)
            return values
        dfs(p, vals1)
        dfs(q, vals2)
        return vals1 == vals2
