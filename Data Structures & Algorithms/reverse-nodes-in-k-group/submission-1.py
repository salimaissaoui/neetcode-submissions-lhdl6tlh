# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k <= 1:
            return head

        # Count up to k nodes
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1

        if count == k:
            # Reverse exactly k nodes
            prev = None
            node = head
            for _ in range(k):
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            # prev is new head of this reversed block
            # node is the start of the next block
            rest = self.reverseKGroup(node, k)
            # original head is now tail of reversed block
            head.next = rest
            return prev
        else:
            return head