#include <vector>
#include <queue>

using namespace std;

class Solution
{

    int INF = 1000000;

public:
    long long totalCost(vector<int> &costs, int k, int candidates)
    {
        int i = 0;
        int j = costs.size() - 1;
        priority_queue<int, vector<int>, greater<int>> pq1;
        priority_queue<int, vector<int>, greater<int>> pq2;

        long long ans = 0;
        while (k > 0)
        {
            while (pq1.size() < candidates && i <= j)
            {
                pq1.push(costs[i]);
                i++;
            }
            while (pq2.size() < candidates && i <= j)
            {
                pq2.push(costs[j]);
                j--;
            }

            int t1 = !pq1.empty() ? pq1.top() : this->INF;
            int t2 = !pq2.empty() ? pq2.top() : this->INF;

            if (t1 <= t2)
            {
                ans += t1;
                pq1.pop();
            }
            else
            {
                ans += t2;
                pq2.pop();
            }

            k--;
        }

        return ans;
    }
};