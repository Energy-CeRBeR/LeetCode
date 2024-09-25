#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution
{
public:
    long long maxScore(vector<int> &nums1, vector<int> &nums2, int k)
    {
        vector<pair<int, int>> pair_nums;
        for (int i = 0; i < nums1.size(); ++i)
        {
            pair_nums.push_back({nums1[i], nums2[i]});
        }
        sort(pair_nums.begin(), pair_nums.end(), [](const pair<int, int> &a, const pair<int, int> &b)
             { return a.second > b.second; });

        priority_queue<int, vector<int>, greater<int>> heap;
        long long s = 0;
        long long result = 0;

        int n1, n2;
        for (auto pair : pair_nums)
        {
            n1 = pair.first;
            n2 = pair.second;
            s += n1;
            heap.push(n1);

            if (heap.size() > k)
            {
                int num = heap.top();
                heap.pop();
                s -= num;
            }

            if (heap.size() == k)
            {
                result = max(result, s * n2);
            }
        }

        return result;
    }
};