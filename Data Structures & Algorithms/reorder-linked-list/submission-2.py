# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next

        n = len(nodes)
        l = 1
        r = n - 1
        temp = head
        while l <= r:
            temp.next = nodes[r]
            temp = temp.next
            r -= 1

            if l <= r:
                temp.next = nodes[l]
                temp = temp.next
                l += 1
            
        temp.next = None