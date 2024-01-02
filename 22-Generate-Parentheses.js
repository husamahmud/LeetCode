/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function (n) {
    const stk = [];
    const res = [];

    function backtrack(opened, closed) {
        // Base case: if the no of the opened and closed parentheses is equal to n
        // add the current combination (stk) to the res array
        if (opened === closed && opened === n) {
            res.push(stk.join(""));
            return;
        }
        // case 1: add an opening parenthesis if the no of opened parenthesis is less than n
        // recursively call backtrack with an increamented count of the opened parentheses
        if (opened < n) {
            stk.push("(");
            backtrack(opened + 1, closed);
            stk.pop();
        }
        // case 2: add a closing parenthesis if the no of closed parenthesis is less than opend
        // recursively call backtrack with an increamented count of the closed parentheses
        if (closed < opened) {
            stk.push(")");
            backtrack(opened, closed + 1);
            stk.pop();
        }
    }

    backtrack(0, 0);
    return res;
};
s
