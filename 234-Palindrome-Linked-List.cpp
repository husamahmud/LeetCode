class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* mid_node = findMid(head);
        ListNode* curr = head;

        mid_node = reverseList(mid_node);

        while (curr && mid_node) {
            if (curr->val != mid_node->val)
                return false;
            curr = curr->next;
            mid_node = mid_node->next;
        }

        return (true);
    }

private:
    ListNode* findMid(ListNode* head) {
        if (head == nullptr || head->next == nullptr)
            return head;

        ListNode* fast = head;
        ListNode* slow = head;

        while (fast->next && fast->next->next) {
            slow = slow->next;
            fast = fast->next->next;
        }

        return (slow->next);
    }

    ListNode* reverseList(ListNode* head) {
        ListNode* prev = nullptr;
        ListNode* curr = head;
        ListNode* next;

        while (curr) {
            next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }

        return (prev);
    }
};