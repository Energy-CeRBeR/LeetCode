#include <algorithm>

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
    int goodNodes(TreeNode *root)
    {
        this->count_good_nodes(root, -100000);

        return this->count;
    }

private:
    int count = 0;

    int count_good_nodes(TreeNode *node, int mx)
    {
        if (node == nullptr)
        {
            return 0;
        }

        this->count += node->val >= mx ? 1 : 0;
        mx = max(mx, node->val);

        return this->count_good_nodes(node->left, mx) + this->count_good_nodes(node->right, mx);
    }
};
