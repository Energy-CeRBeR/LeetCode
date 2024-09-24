#include <vector>
#include <queue>

using namespace std;

class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        priority_queue<int> heap;

        for (auto item : nums)
        {
            heap.push(item);
        }

        for (int i = 0; i < k - 1; ++i)
        {
            heap.pop();
        }

        return heap.top();
    }
};