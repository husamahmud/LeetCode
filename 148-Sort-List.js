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
var sortList = function (head) {
    let curr = head,
        values = [];

    while (curr !== null) {
        values.push(curr.val);
        curr = curr.next;
    }

    values.sort((a, b) => b - a);

    let sortedLL = new ListNode(0);
    let dummy = sortedLL;

    while (values.length !== 0) {
        let x = values.pop();
        sortedLL.next = new ListNode(x);
        sortedLL = sortedLL.next;
    }

    return dummy.next;
};
