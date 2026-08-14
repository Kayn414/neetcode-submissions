# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        prev = None # input is say [1,2,3,4,5]
        curr = slow.next # points the second half to list 1 .e.g (4)
        slow.next = None # reverse the second half 1 ,2, 3  | 4, 5

        while curr:
            next_temp = curr.next # 5, None
            curr.next = prev # None, 4
            prev = curr # 4, 5 
            curr = next_temp # 5, None
        

        first = head # 1
        second = prev # 5 

        while second:
            tmp1 = first.next # 2 
            tmp2  = second.next # 4 

            first.next = second # 1 -> 5
            second.next = tmp1 # 1 -> 5 -> 2 -> 3

            first = tmp1 # 2
            second = tmp2 # 4

    

        