# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = 0

        temp = head
        while temp:
            temp = temp.next
            k += 1
        
        curr = head
        stop = k - n
        ind = 0

        if stop == 0:
            return head.next
        
        while curr:
            if ind == stop - 1:
                curr.next = curr.next.next
                return head
            ind += 1
            curr = curr.next
        
        return head