#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int candy(vector<int> &ratings)
    {
        int n = ratings.size();
        if (n == 1)
            return 1;

        vector<int> dp(n, 1);
        for (int i = 1; i < n; ++i)
        {
            if (ratings[i] > ratings[i - 1])
                dp[i] = dp[i - 1] + 1;
        }

        int count = dp[n - 1];
        for (int i = n - 1; i > 0; --i)
        {
            if (ratings[i] < ratings[i - 1])
                dp[i - 1] = max(dp[i - 1], dp[i] + 1);
            count += dp[i - 1];
        }

        return count;
    }
};