/**
 * Definition for singly-linked list.
 */
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val);
    this.next = (next === undefined ? null : next);
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function (head) {
    let dummy = new ListNode(0);
    dummy.next = head;
    let curr = dummy;

    while (curr.next && curr.next.next) {
        let first = curr.next,
            second = curr.next.next;

        // swapping
        first.next = second.next;
        second.next = first;
        curr.next = second;

        // move curr ptr two nodes ahead
        curr = curr.next.next;
    }

    return dummy.next;
};
