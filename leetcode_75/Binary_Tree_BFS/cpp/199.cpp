#include <vector>
#include <deque>

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
    vector<int> rightSideView(TreeNode *root)
    {
        if (root == nullptr)
        {
            return {};
        }

        vector<int> result;
        deque<TreeNode *> q = {root};
        TreeNode *node = nullptr;
        while (!q.empty())
        {
            int q_size = q.size();
            for (int i = 0; i < q_size; ++i)
            {
                node = q.front();
                q.pop_front();
                if (node->left)
                {
                    q.push_back(node->left);
                }
                if (node->right)
                {
                    q.push_back(node->right);
                }
            }
            result.push_back(node->val);
        }

        return result;
    }
};