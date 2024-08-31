#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    double findMaxAverage(vector<int> &nums, int k)
    {
        int cur_s = 0;
        for (int i = 0; i < k; ++i)
        {
            cur_s += nums[i];
        }
        int mx_sum = cur_s;

        for (int i = k; i < nums.size(); ++i)
        {
            cur_s += nums[i] - nums[i - k];
            mx_sum = max(mx_sum, cur_s);
        }

        
        return (double)mx_sum / k;
    }
};
