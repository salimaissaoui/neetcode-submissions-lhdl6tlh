# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestors = defaultdict(list)

        # Perform Binary Search for p and q
        def search(root, target):
            curr = root
            h = 0
            while curr:
                ancestors[target].append((curr, h))
                if target == curr.val:
                    return curr
                elif target < curr.val:
                    curr = curr.left
                    h += 1
                else:
                    curr = curr.right
                    h += 1
            return None
        
        search(root, p.val)
        search(root, q.val)
        common = set(ancestors[p.val]) & set(ancestors[q.val])
        
        res = max(common, key=lambda x: x[1])
            


        
        return res[0]

            
        