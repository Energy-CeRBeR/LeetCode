#include <vector>

using namespace std;

class Solution
{
public:
    vector<int> productExceptSelf(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> p1(n, 1);
        vector<int> p2(n, 1);

        for (int i = 1; i < n; ++i)
        {
            p1[i] = p1[i - 1] * nums[i - 1];
            p2[i] = p2[i - 1] * nums[n - i];
        }

        vector<int> result;
        for (int i = 0; i < n; ++i)
        {
            result.push_back(p1[i] * p2[n - i - 1]);
        }

        return result;
    }
};