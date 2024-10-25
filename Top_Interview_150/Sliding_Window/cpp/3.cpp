#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_map<char, int> hash_table;
        int start = 0;
        int mx = 0;

        for (int i = 0; i < s.size(); ++i)
        {
            if (hash_table.find(s[i]) != hash_table.end() && hash_table[s[i]] >= start)
                start = hash_table[s[i]] + 1;
            hash_table[s[i]] = i;
            mx = max(mx, i - start + 1);
        }

        return mx;
    }
};