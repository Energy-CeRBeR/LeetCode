#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int maxProfit(vector<int> &prices)
    {
        int n = prices.size();
        vector<pair<int, int>> dp(n);
        dp[0] = {-prices[0], 0};

        for (int i = 1; i < n; ++i)
        {
            dp[i].first = max(dp[i - 1].second - prices[i], dp[i - 1].first);
            dp[i].second = max(dp[i - 1].first + prices[i], dp[i - 1].second);
        }

        return max(dp[n - 1].first, dp[n - 1].second);
    }
};