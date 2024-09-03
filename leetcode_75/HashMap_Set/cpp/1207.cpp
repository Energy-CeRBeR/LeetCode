#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution
{
public:
    bool uniqueOccurrences(vector<int> &arr)
    {
        unordered_map<int, int> m;
        for (auto num : arr)
        {
            if (m.count(num) == 0)
            {
                m[num] = 0;
            }
            m[num] += 1;
        }

        std::vector<int> values;
        for (auto const &[key, value] : m)
        {
            values.push_back(value);
        }

        unordered_set<int> d(values.begin(), values.end());
        if (values.size() == d.size())
        {
            return true;
        }
        return false;
    }
};