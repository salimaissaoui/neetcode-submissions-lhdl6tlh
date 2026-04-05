"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Create a dictionary to map original nodes to copied nodes
        node_map = {}

        # First pass: create new nodes and store them in the map
        curr = head
        while curr:
            node_map[curr] = Node(curr.val)
            curr = curr.next

        # Second pass: set the next and random pointers of the copied nodes
        curr = head
        while curr:
            copied_node = node_map[curr]
            copied_node.next = node_map.get(curr.next)
            copied_node.random = node_map.get(curr.random)
            curr = curr.next

        return node_map[head]