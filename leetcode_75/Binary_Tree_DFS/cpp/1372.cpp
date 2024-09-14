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
    int longestZigZag(TreeNode *root)
    {
        return max(this->helper(root->right, 0, true), this->helper(root->left, 0, false));
    }

private:
    int helper(TreeNode *node, int count, bool to_right)
    {
        if (node == nullptr)
        {
            return count;
        }

        count++;
        if (to_right)
        {
            return max(this->helper(node->left, count, false), this->helper(node->right, 0, true));
        }
        else
        {
            return max(this->helper(node->right, count, true), this->helper(node->left, 0, false));
        }
    }
};