"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    prev = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev