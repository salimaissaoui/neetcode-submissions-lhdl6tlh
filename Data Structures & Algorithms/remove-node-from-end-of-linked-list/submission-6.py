# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        cur = head
        i = 0
        prev = cur
        lenlist = 0
        current = head
        while current:
            lenlist+=1
            current = current.next
        print(lenlist)
            
        
        if lenlist == 1:
            return None


        dummy = ListNode(-1)
        dummy.next = head
        while cur:
            if i == lenlist - n and i != 0:
                prev.next = cur.next
            if i == lenlist - n and i == 0:
                dummy.next = cur.next
            prev = cur
            i +=1
            cur = cur.next
        return dummy.next


        

        # cur = head
        # prev = None
        # current = head
        # i = 0
        # while current:
        #     current = current.next
        #     i+=1
        
        # j = 0
        # while cur:
        #     if j >= i-n:
        #         next_node = cur.next
        #         cur.next = None
        #         cur = next_node
        #     else:
        #         cur = cur.next
        #     j+=1
        # return head







        






        
        
        