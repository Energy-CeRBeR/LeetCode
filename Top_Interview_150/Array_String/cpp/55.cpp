#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        int n = nums.size();
        int max_index = 0;

        for (int i = 0; i < n - 1; ++i)
        {
            if (i <= max_index)
                max_index = max(max_index, i + nums[i]);
        }

        return n - 1 <= max_index;
    }
};