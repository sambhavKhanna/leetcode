struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* removeNthFromEnd(ListNode* head, int n) {
    int length = 0;
    ListNode *ptr = head;
    while (ptr) { ptr = ptr->next; ++length; }
    ListNode *curr = head;
    ListNode *back = nullptr;
    for(int i = 1; i < length - n + 1; i++) {
        back = curr;
        curr = curr->next;
    }
    if (back) { back->next = curr->next; return head; }
    else { head = head->next; return head; }
}