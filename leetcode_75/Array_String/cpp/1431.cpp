#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<bool> kidsWithCandies(vector<int> &candies, int extraCandies)
    {
        int base_mx = 0;
        for (auto c : candies)
        {
            base_mx = max(base_mx, c);
        }

        vector<bool> result(candies.size());
        for (int i = 0; i < candies.size(); ++i)
        {
            result[i] = candies[i] + extraCandies >= base_mx ? true : false;
        }

        return result;
    }
};