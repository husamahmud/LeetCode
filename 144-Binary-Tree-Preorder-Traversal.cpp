class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
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

        res.push_back(root->val);
        traversal(res, root->left);
        traversal(res, root->right);
    }
};