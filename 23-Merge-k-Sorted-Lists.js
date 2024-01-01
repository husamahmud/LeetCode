/**
 * Definition for singly-linked list.
 */
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val);
    this.next = (next === undefined ? null : next);
}

/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {
    let dummy = new ListNode(),
        curr = dummy;

    while (list1 && list2) {
        if (list1.val > list2.val) {
            curr.next = list2;
            list2 = list2.next;
        } else {
            curr.next = list1;
            list1 = list1.next;
        }
        curr = curr.next;
    }

    if (list1) curr.next = list1;
    if (list2) curr.next = list2;

    return dummy.next;
};

/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
    let head = null;

    for (let i = 0; i < lists.length; i++)
        head = mergeTwoLists(head, lists[i]);

    return head;
};
