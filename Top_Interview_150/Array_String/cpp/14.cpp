#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        sort(strs.begin(), strs.end());
        string left = strs[0];
        string right = strs[strs.size() - 1];

        int length = min(left.size(), right.size());
        string result = "";
        for (int i = 0; i < length; ++i)
        {
            if (left[i] == right[i])
                result += left[i];
            else
                return result;
        }

        return result;
    }
};