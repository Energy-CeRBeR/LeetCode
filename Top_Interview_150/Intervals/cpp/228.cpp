#include <vector>
#include <string>

using namespace std;

class Solution
{
public:
    vector<string> summaryRanges(vector<int> &nums)
    {
        int n = nums.size();
        if (!n)
            return {};

        int left = nums[0];
        vector<string> result;
        for (int i = 1; i < n; ++i)
        {
            if ((long)nums[i] - (long)nums[i - 1] > 1)
            {
                if (left == nums[i - 1])
                    result.push_back(to_string(left));
                else
                    result.push_back(to_string(left) + "->" + to_string(nums[i - 1]));
                left = nums[i];
            }
        }

        if (left == nums[n - 1])
            result.push_back(to_string(left));
        else
            result.push_back(to_string(left) + "->" + to_string(nums[n - 1]));

        return result;
    }
};