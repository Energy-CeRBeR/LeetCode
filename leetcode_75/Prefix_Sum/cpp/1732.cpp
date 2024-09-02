#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int largestAltitude(vector<int> &gain)
    {
        int cur_height = 0;
        int mx = 0;
        for (auto dh : gain)
        {
            cur_height += dh;
            mx = max(mx, cur_height);
        }

        return mx;
    }
};