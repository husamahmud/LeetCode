class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (!root)
            return 0;

        int lMaxDepth = maxDepth(root->left);
        int rMaxDepth = maxDepth(root->right);

        return max(lMaxDepth, rMaxDepth) + 1;
    }
};