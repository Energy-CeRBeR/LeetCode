#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution
{
public:
    vector<vector<int>> findDifference(vector<int> &nums1, vector<int> &nums2)
    {
        unordered_set<int> a(nums1.begin(), nums1.end());
        unordered_set<int> b(nums2.begin(), nums2.end());

        vector<vector<int>> result(2);

        for (auto num : a)
        {
            if (b.find(num) == b.end())
            {
                result[0].push_back(num);
            }
        }

        for (auto num : b)
        {
            if (a.find(num) == a.end())
            {
                result[1].push_back(num);
            }
        }

        return result;
    }
};