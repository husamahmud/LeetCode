class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == nullptr)
            return {};

        vector<int> res;
        traversal(res, root);
        return res;
    }

private:
    void traversal(vector<int>& res, TreeNode* root) {
        if (root == nullptr)
            return;

        traversal(res, root->left);
        res.push_back(root->val);
        traversal(res, root->right);
    }
};