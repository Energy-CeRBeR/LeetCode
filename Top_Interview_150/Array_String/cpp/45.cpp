#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int jump(vector<int> &nums)
    {
        int count = 0;
        int last = 0;
        int max_index = 0;

        for (int i = 0; i < nums.size() - 1; ++i)
        {
            max_index = max(max_index, i + nums[i]);

            if (i == last)
            {
                last = max_index;
                count++;
            }
        }

        return count;
    }
};