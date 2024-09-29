#include <vector>

using namespace std;

class Solution
{
public:
    int numTilings(int n)
    {
        if (n < 3)
        {
            return n;
        }

        vector<long> dp(n + 1, 0);

        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;

        for (int i = 3; i < n + 1; ++i)
        {
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % (1000000000 + 7);
        }

        return dp[n];
    }
};