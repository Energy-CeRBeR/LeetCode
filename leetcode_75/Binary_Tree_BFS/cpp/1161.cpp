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
    int maxLevelSum(TreeNode *root)
    {
        int mx_val = -1000000;
        int level = 0;

        int k = 0;
        int s, q_size;
        deque<TreeNode *> q = {root};
        TreeNode *node = nullptr;
        while (!q.empty())
        {
            k++;
            s = 0;
            q_size = q.size();
            for (int i = 0; i < q_size; ++i)
            {
                node = q.front();
                s += node->val;
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
            if (s > mx_val)
            {
                mx_val = s;
                level = k;
            }
        }

        return level;
    }
};