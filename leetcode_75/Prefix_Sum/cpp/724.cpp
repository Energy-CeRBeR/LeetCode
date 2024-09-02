#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    int pivotIndex(vector<int> &nums)
    {
        int s = 0;
        for (auto num : nums)
        {
            s += num;
        }

        int ps = 0;
        for (int i = 0; i < nums.size(); ++i)
        {
            if (ps == s - ps - nums[i])
            {
                return i;
            }
            ps += nums[i];
        }

        return -1;
    }
};