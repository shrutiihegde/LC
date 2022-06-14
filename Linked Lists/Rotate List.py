# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        
        # create ring
        old_tail = head
        num_nodes = 1
        while old_tail.next:
            old_tail = old_tail.next
            num_nodes += 1
        old_tail.next = head
        
        # find new tail : (num_nodes - k % n - 1)th node
        # and new head : (num_nodes - k % n)th node
        
        new_tail = head
        for i in range(num_nodes - k % num_nodes - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # break the ring
        new_tail.next = None
        
        return new_head
            
