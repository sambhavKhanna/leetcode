"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    cur1 = list1
    cur2 = list2
    head = ListNode()
    cur = head
    while cur1 and cur2:
        if cur1.val <= cur2.val:
            cur.next = cur1
            cur = cur.next
            cur1 = cur1.next
        elif cur1.val > cur2.val:
            cur.next = cur2
            cur = cur.next
            cur2 = cur2.next
    if cur1:
        cur.next = cur1
    elif cur2:
        cur.next = cur2
    head = head.next
    return head