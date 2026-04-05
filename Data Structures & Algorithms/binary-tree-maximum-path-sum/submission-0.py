# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #postorder traversal
        max_sum = float('-infinity')
        def dfs(node) -> int: # return the max path sum from the node to the leaf
            if not node:
                return 0
            nonlocal max_sum
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))      
            max_sum = max(max_sum, node.val + left_sum + right_sum)
            return max(left_sum, right_sum) + node.val
        dfs(root)
        return max_sum
    
    