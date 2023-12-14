# created by ymirwani

# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(-1)
        cur = res
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            v = v1 + v2 + carry
            carry = v//10
            v = v % 10
            cur.next = ListNode(v)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return res.next
    

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    lsum = ListNode(7)
    lsum.next = ListNode(0)
    lsum.next.next = ListNode(8)
    result = Solution().addTwoNumbers(l1, l2)

    # Check if the result matches the expected linked list
    while result:
        if result.val != lsum.val:
            print("Test failed: Result does not match expected linked list.")
            break
        result = result.next
        lsum = lsum.next
    else:
        print("Test passed: Result matches expected linked list.")