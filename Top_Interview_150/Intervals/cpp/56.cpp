#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<vector<int>> merge(vector<vector<int>> &intervals)
    {
        int n = intervals.size();
        sort(intervals.begin(), intervals.end(),
             [](const vector<int> &a, const vector<int> &b)
             {
                 if (a[0] != b[0])
                 {
                     return a[0] < b[0];
                 }
                 return a[1] > b[1];
             });

        vector<vector<int>> result;
        int left = intervals[0][0];
        int right = intervals[0][1];
        for (int i = 1; i < n; ++i)
        {
            if (intervals[i][0] > right)
            {
                result.push_back({left, right});
                left = intervals[i][0];
                right = intervals[i][1];
            }
            else
                right = max(right, intervals[i][1]);
        }
        result.push_back({left, right});

        return result;
    }
};