# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        for _ in range(n + 1): # n=2 move three steps, fast = 3
            fast = fast.next

        while fast: # 3
            slow = slow.next # 1, 2, 3,
            fast = fast.next # 4, ,5 , None
        

        slow.next = slow.next.next #1 , 2,3 ,5

        return dummy.next

