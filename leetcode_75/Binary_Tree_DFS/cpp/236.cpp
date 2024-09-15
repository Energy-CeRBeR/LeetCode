struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution
{
public:
    TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q)
    {
        if (root == nullptr)
        {
            return nullptr;
        }

        if (root == p || root == q)
        {
            return root;
        }

        TreeNode *left_lca = this->lowestCommonAncestor(root->left, p, q);
        TreeNode *right_lca = this->lowestCommonAncestor(root->right, p, q);

        if (left_lca != nullptr && right_lca != nullptr)
        {
            return root;
        }

        return left_lca != nullptr ? left_lca : right_lca;
    }
};