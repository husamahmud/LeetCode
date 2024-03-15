class Solution {
public:
    bool isValid(string s) {
        stack<char> stk;

        for (char c : s) {
            if (c == '[' || c == '{' || c == '(')
                stk.push(c);
            else {
                if (stk.empty())
                    return false;

                char top = stk.top();
                stk.pop();

                if ((top == '[' && c != ']') || 
                    (top == '{' && c != '}') ||
                    (top == '(' && c != ')'))
                    return false;
            }
        }

        return stk.empty();
    }
};