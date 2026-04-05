# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0

        while l1:
            num1 *= 10
            num1 += l1.val
            l1 = l1.next
        
        while l2:
            num2 *= 10
            num2 += l2.val
            l2 = l2.next
        
        num1 = int(str(num1)[::-1])
        num2 = int(str(num2)[::-1])
        num3 = str(num1 + num2)[::-1]
        nodes = []
        for char in num3:
            nodes.append(int(char))
        
        l3 = ListNode(-1)
        dummy = l3

        for num in nodes:
            l3.next = ListNode(num)
            l3 = l3.next
        
        return dummy.next
