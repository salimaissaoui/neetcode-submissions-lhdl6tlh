# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        head = ListNode(-1)
        dummy = head

        while heap:
            val, i, nextnode = heapq.heappop(heap)
            head.next = nextnode
            head = head.next
            if nextnode.next:
                heapq.heappush(heap, (nextnode.next.val, i, nextnode.next))

        return dummy.next