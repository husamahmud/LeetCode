class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* next;

        return reverse(curr, next, prev);
    }

private:
    ListNode* reverse(ListNode* curr, ListNode* next, ListNode* prev) {
        if (curr == nullptr)
            return prev;

        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;

        return reverse(curr, next, prev);
    };
};