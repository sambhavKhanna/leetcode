"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
"""

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head
    cur = head
    head = head.next
    while True:
        if not cur.next.next:
            cur.next.next = cur
            cur.next = None
            break
        if not cur.next.next.next:
            temp = cur.next.next
            cur.next.next = cur
            cur.next = temp
            break
        temp = cur.next.next
        cur.next.next = cur
        cur.next = temp.next
        cur = temp
    
    return head