#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        unordered_map<string, vector<string>> d;
        for (string s : strs)
        {
            string sorted_s = s;
            sort(sorted_s.begin(), sorted_s.end());
            d[sorted_s].push_back(s);
        }

        vector<vector<string>> result;
        for (const auto &[key, value] : d)
        {
            result.push_back(value);
        }

        return result;
    }
};