#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int rob(vector<int> &nums)
    {
        int n = nums.size();
        vector<pair<int, int>> dp(n, {0, 0});
        dp[0].second = nums[0];

        for (int i = 1; i < n; ++i)
        {
            dp[i].first = max(dp[i - 1].first, dp[i - 1].second);
            dp[i].second = dp[i - 1].first + nums[i];
        }

        return max(dp[n - 1].first, dp[n - 1].second);
    }
};