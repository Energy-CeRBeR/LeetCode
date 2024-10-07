#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int n = prices.size();
        vector<pair<int, int>> dp;
        dp.push_back({-prices[0], 0});

        for (int i = 1; i < n; ++i)
        {
            dp.push_back({max(dp[i - 1].first, -prices[i]), max(dp[i - 1].second, dp[i - 1].first + prices[i])});
        }

        return dp[n - 1].second;
    }
};