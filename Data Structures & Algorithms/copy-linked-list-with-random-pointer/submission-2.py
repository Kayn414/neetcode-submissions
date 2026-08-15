"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# other solution uses the orignial linked object via interweaving copies and assigns the correct pointers.
# optimizes the problem to allocate O(1) memory usage to just fit a local solution, rather than the hashmap global allocation of thats grows to O(n) object size
#  # 1. Interweave copies
    # cur = head
    # while cur:
    #     copy = Node(cur.val, cur.next)
    #     cur.next = copy
    #     cur = copy.next

    # # 2. Assign random pointers for the copies
    # cur = head
    # while cur:
    #     if cur.random:
    #         cur.next.random = cur.random.next
    #     cur = cur.next.next

    # # 3. Separate the two lists
    # dummy = Node(0)
    # copy_cur = dummy
    # cur = head
    # while cur:
    #     copy = cur.next
    #     cur.next = copy.next          # restore original
    #     copy_cur.next = copy
    #     copy_cur = copy
    #     cur = cur.next

    # return dummy.next

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # copy all values into new linked list 
        new_ll = {}
        curr = head
        while curr:
            new_ll[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head 
        while curr:
            if curr.next:
                new_ll[curr].next = new_ll[curr.next]
            if curr.random:
                new_ll[curr].random = new_ll[curr.random]
            curr = curr.next
        return new_ll[head]