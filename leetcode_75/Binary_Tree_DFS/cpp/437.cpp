
struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution
{
public:
    int pathSum(TreeNode *root, int targetSum)
    {
        this->targetSum = targetSum;

        return this->helper(root);
    }

private:
    int targetSum;

    int get_sum(TreeNode *node, long int s)
    {
        if (node == nullptr)
        {
            return 0;
        }

        s += node->val;
        return (s == this->targetSum) + this->get_sum(node->left, s) + this->get_sum(node->right, s);
    }

    int helper(TreeNode *node)
    {
        if (node == nullptr)
        {
            return 0;
        }
        return this->get_sum(node, 0) + this->helper(node->left) + this->helper(node->right);
    }
};