#include <vector>

using namespace std;

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
    int get_leaves(TreeNode *node, vector<int> &leaves)
    {
        if (node == nullptr)
        {
            return 0;
        }
        if (node->left == nullptr && node->right == nullptr)
        {
            leaves.push_back(node->val);
            return 0;
        }
        return this->get_leaves(node->left, leaves) + this->get_leaves(node->right, leaves);
    }

    bool leafSimilar(TreeNode *root1, TreeNode *root2)
    {
        vector<int> t1;
        vector<int> t2;
        this->get_leaves(root1, t1);
        this->get_leaves(root2, t2);

        return t1 == t2;
    }
};