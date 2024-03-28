class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root == nullptr)
            return nullptr;

        TreeNode* temp = root->left;
        
        invertTree(root->left);
        invertTree(root->right);

        root->left = root->right;
        root->right = temp;

        return root;
    }
};