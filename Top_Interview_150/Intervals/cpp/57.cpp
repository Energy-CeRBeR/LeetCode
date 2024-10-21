#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<vector<int>> insert(vector<vector<int>> &intervals, vector<int> &newInterval)
    {
        int n = intervals.size();
        if (n == 0)
            return {newInterval};

        vector<vector<int>> new_intervals;
        int ptr = 0;
        while (ptr < n && intervals[ptr][0] < newInterval[0])
            new_intervals.push_back(intervals[ptr++]);

        if (!new_intervals.empty() && new_intervals.back()[1] >= newInterval[0])
            new_intervals.back()[1] = max(new_intervals.back()[1], newInterval[1]);
        else
            new_intervals.push_back(newInterval);

        while (ptr < n)
        {
            if (intervals[ptr][0] > new_intervals.back()[1])
                new_intervals.push_back(intervals[ptr]);
            else
                new_intervals.back()[1] = max(new_intervals.back()[1], intervals[ptr][1]);
            ptr++;
        }

        return new_intervals;
    }
};
