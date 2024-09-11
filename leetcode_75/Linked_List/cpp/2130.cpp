#include <vector>
#include <algorithm>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

    class Solution
    {
    public:
        int pairSum(ListNode *head)
        {
            vector<int> stack;
            ListNode *cur_obj = head;
            while (cur_obj != nullptr)
            {
                stack.push_back(cur_obj->val);
                cur_obj = cur_obj->next;
            }

            int mx = 0;
            int size = stack.size();
            for (int i = 0; i < size / 2; ++i)
            {
                mx = max(mx, stack[i] + stack[size - i - 1]);
            }

            return mx;
        }
    };