from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize variables to store the result and carry
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both linked lists simultaneously
        while l1 or l2:
            # Get the values of the current nodes or 0 if node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            
            # Move to the next nodes if they exist
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Handle the remaining carry, if any
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the result linked list starting from the next of dummy head
        return dummy_head.next
