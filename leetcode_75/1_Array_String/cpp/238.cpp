#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> pref1 = {1};
        vector<int> pref2 = {1};
        for (int i = 0; i < n; i++)
        {
            pref1.push_back(pref1[i] * nums[i]);
            pref2.push_back(pref2[i] * nums[n - i - 1]);
        }
        reverse(pref2.begin(), pref2.end());

        vector<int> result;
        for (int i = 0; i < n; i++)
        {
            result.push_back(pref1[i] * pref2[i + 1]);
        }

        return result;
    }
};